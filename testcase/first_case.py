import time

import minium


class FirstTest(minium.MiniTest):
    def test_get_system_info(self):
        sys_info = self.mini.get_system_info()
        self.logger.info(f'SDKVersion is: {sys_info.get("SDKVersion")}')
        self.assertIn("SDKVersion", sys_info)

    def test_input_phone(self):
        # 跳转到指定页面
        self.app.navigate_to("/pages/others/form/form")
        # 获取当前页面
        page = self.app.get_current_page()
        # 指定等待时间
        page.wait_for(10)
        # 根据class获取元素 tagname.classname
        e = page.get_element("view.weui-vcode-btn")
        e.tap()
