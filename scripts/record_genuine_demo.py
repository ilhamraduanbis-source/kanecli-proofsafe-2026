#!/usr/bin/env python3
"""Record genuine live Chromium interactions against this repository's local app.

This is Playwright/Chromium footage, NOT KaneCLI footage, physical hardware or
fabricated browser action. Kane CLI has separate original artifacts.
"""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright
import time

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

root = Path(__file__).resolve().parents[1]
out = root / "evidence" / "browser-demo"
out.mkdir(parents=True, exist_ok=True)
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Quiet, directory=str(root)))
Thread(target=server.serve_forever, daemon=True).start()

try:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, args=['--no-sandbox'])
        context = browser.new_context(
            viewport={'width':1280,'height':720},
            record_video_dir=str(out),
            record_video_size={'width':1280,'height':720},
            accept_downloads=True
        )
        page = context.new_page()
        page.goto(f'http://127.0.0.1:{server.server_port}/', wait_until='networkidle')
        assert page.get_by_role('heading', name='Test the claim. Keep the evidence.').is_visible()
        video = page.video
        time.sleep(5)

        assert page.locator('#download').is_disabled()
        page.screenshot(path=str(out/'before.png'))
        time.sleep(3)
        page.get_by_role('button', name='Validate locally').click()
        assert 'PASS' in page.locator('#status').inner_text()
        assert page.locator('#rows').inner_text() == '2'
        page.screenshot(path=str(out/'valid-pass.png'))
        time.sleep(7)

        assert page.locator('#download').is_enabled()
        with page.expect_download() as download:
            page.get_by_role('button', name='Export reproducible JSON').click()
        assert download.value.suggested_filename == 'proofsafe-local-validation.json'
        time.sleep(5)

        page.get_by_role('button', name='Load failing case').click()
        assert page.locator('#download').is_disabled()
        time.sleep(3)
        page.get_by_role('button', name='Validate locally').click()
        assert 'FAIL' in page.locator('#status').inner_text()
        assert page.locator('#issues').inner_text() == '3'
        page.screenshot(path=str(out/'invalid-fail.png'))
        time.sleep(7)

        page.get_by_role('button', name='Reset sample').click()
        time.sleep(3)
        page.get_by_role('button', name='Validate locally').click()
        assert 'PASS' in page.locator('#status').inner_text()
        page.screenshot(path=str(out/'reset-pass.png'))
        time.sleep(6)

        context.close()
        video.save_as(str(out/'genuine-browser-interactions.webm'))
        browser.close()
        assert (out/'genuine-browser-interactions.webm').stat().st_size > 10000
        print('GENUINE_PLAYWRIGHT_BROWSER_VIDEO_PASS',
              (out/'genuine-browser-interactions.webm').stat().st_size)
finally:
    server.shutdown()
