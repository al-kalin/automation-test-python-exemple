from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindows:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            browser_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_window_page.open()
            text_result = browser_window_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', 'A new tab has not opened or incorrect tab has opened'

        def test_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_window_page.open()
            text_result = browser_window_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', 'A new tab window not opened or incorrect window has opened'
