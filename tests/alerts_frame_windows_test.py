from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage


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

    class TestAlertsPage:

        def test_see_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == 'You clicked a button', "Alert did not show up"

        def test_alert_appear_5_sec(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', "Alert did not show up"

        def test_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', "Alert did not show up"

        def test_prompt_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            text, alert_text = alerts_page.check_prompt_alert()
            print(text)
            print(alert_text)
            assert alert_text == 'You entered ' + text, "Alert did not show up"

    class TestFramesPage:
        def test_frames(self, driver):
            frames_page = FramesPage(driver, "https://demoqa.com/frames")
            frames_page.open()
            result_frame1 = frames_page.check_frame('frame1')
            result_frame2 = frames_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame does not exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame does not exist"

    class TestNestedFramesPage:
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frames_page.open()
            parent_text, child_text = nested_frames_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'
