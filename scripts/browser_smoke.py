#!/usr/bin/env python3
"""Genuine Chromium UI test; not KaneCLI."""
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
root=Path(__file__).resolve().parents[1]
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(root)))
Thread(target=server.serve_forever,daemon=True).start()
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None,args=['--no-sandbox'])
  page=browser.new_page(viewport={'width':1200,'height':820},accept_downloads=True)
  page.goto('http://127.0.0.1:'+str(server.server_port)+'/')
  assert page.get_by_role('heading',name='Test the claim. Keep the evidence.').count()==1
  assert page.locator('#download').is_disabled()
  page.get_by_role('button',name='Validate locally').click()
  assert 'PASS' in page.locator('#status').inner_text()
  assert page.locator('#rows').inner_text()=='2'
  assert page.locator('#download').is_enabled()
  with page.expect_download() as d:page.get_by_role('button',name='Export reproducible JSON').click()
  assert d.value.suggested_filename=='proofsafe-local-validation.json'
  # KaneCLI's first real run confirmed PASS/FAIL and reset, but did not
  # inspect the exported JSON. This is the explicit feedback coverage gap.
  from tempfile import TemporaryDirectory
  import json
  with TemporaryDirectory() as folder:
   sample_path=Path(folder)/'valid.json'
   d.value.save_as(str(sample_path))
   exported=json.loads(sample_path.read_text())
   assert exported['ok'] is True and exported['rows']==2
   assert exported['source']=='LOCAL_BROWSER'
   assert exported['verifiedByKane'] is False
   assert exported['transactionSettled'] is False
   assert 'input' not in exported
   assert 'invoice_id' not in json.dumps(exported)
  page.get_by_role('button',name='Load failing case').click()
  assert page.locator('#download').is_disabled()
  page.get_by_role('button',name='Validate locally').click()
  assert 'FAIL' in page.locator('#status').inner_text()
  assert int(page.locator('#issues').inner_text())>=2
  page.get_by_role('button',name='Reset sample').click()
  page.get_by_role('button',name='Validate locally').click()
  assert 'PASS' in page.locator('#status').inner_text()
  proof=root/'docs'/'browser-qa-local.png'
  proof.parent.mkdir(parents=True,exist_ok=True)
  page.screenshot(path=str(proof),full_page=True)
  print('REAL_CHROMIUM_UI_PASS',proof)
  browser.close()
finally:server.shutdown()
