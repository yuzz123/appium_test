class Common:
    """
    封装通用的方法
    """

    def __init__(self):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read('enable_data.conf')

    def cycle_screen(self, section_name, num, driver):
        """
        循环截图功能
        从json文件中读取信息,用来定位点击的方位和保存截图的路径
        执行成功则返回True,否则返回False
        :param section_name: json文件中一级节点的名称
        :param num: json文件中对应的列表序列位
        :param driver: Appium的驱动
        :return:True or False
        """
        try:
            with open('get_screen.json', 'r') as f:
                jsondata = f.read()
            cx_info = json.loads(jsondata)
            values = cx_info[section_name][num].values()
            for value in values:
                driver.get_name(value['name']).click()
                time.sleep(2)
                self.check_title(value['name'], driver)
                driver.get_screen(value['path'])
                logging.info(value['log'])
            return True
        except Exception as e:
            logging.warning(e)
            return False

    def cycle_screen_and_back(self, section_name, num, driver):
        """
        功能和上一个函数一样,在步骤最后加了一个返回事件,用来处理"行情"-"更多"页面的数据校验
        :param section_name: conf配置文件的节点名称
        """
        try:
            with open('get_screen.json', 'r') as f:
                jsondata = f.read()
            cx_info = json.loads(jsondata)
            values = cx_info[section_name][num].values()
            for value in values:
                logging.info(value)
                driver.get_name(value['name']).click()
                time.sleep(2)
                self.check_title(value['name'], driver)
                # title = driver.get_classes('android.widget.TextView')[0].text
                # try:
                #     assert title == value['name']
                #     logging.info(title + '页面显示正确')
                # except Exception as e:
                #     logging.warning(value['name'])
                #     logging.warning(title + '页面显示不正确')
                driver.get_screen(value['path'])
                driver.driver.keyevent(4)
                time.sleep(1)
                logging.info(value['log'])
            return True
        except Exception as e:
            logging.warning(e)
            return False

    def check_title(self, title, driver):
        text = driver.get_classes('android.widget.TextView')[0].text
        try:
            assert text == title
            logging.info("标题为: {} 校验通过".format(title))
            return True
        except Exception as e:
            logging.warning(e)
            logging.warning("标题为: {} 校验不通过".format(title))
            return False

    def compare(self, ids, numstar, numend, driver):
        """
        比较传入值得大小, 第一个数比第二个数大返回True,否则返回False
        :param ids:传入的ID名
        :param numstar:传入的开始序号
        :param numend:传入的结束需要
        :param driver:驱动
        :return:True or False
        """
        try:
            startext = float(driver.get_ids(ids)[numstar].text)
            endtext = float(driver.get_ids(ids)[numend].text)
        except ValueError:
            starmark = driver.get_ids(ids)[numstar].text[:1]
            endmark = driver.get_ids(ids)[numend].text[:1]
            if starmark == endmark:
                startext = float(driver.get_ids(ids)[numstar].text.lstrip(starmark).rstrip('%'))
                endtext = float(driver.get_ids(ids)[numend].text.lstrip(endmark).rstrip('%'))
            elif starmark == "+":
                return True
            elif starmark == "-":
                return False
        if startext > endtext:
            return True
        else:
            return False

    def get_SotckCode(self, ids, driver):
        """
        获取行情-自选页面中的所有股票代码,自选超过50支的时候请修改参数中的range(10)
        返回list
        :param driver:驱动控件
        :return:list, 自选股票代码
        """
        SotckCode = []
        for x in driver.get_ids(ids):
            SotckCode.append(x.text)
        for x in range(5):
            driver.swipe_to_up()
            for x in driver.get_ids(ids):
                if x.text not in SotckCode:
                    SotckCode.append(x.text)
        return SotckCode

    def zjzh_login(self, driver):
        """
        资金账号登录方法,传入appium-driver
        APP启动时需要资金账号为登录状态时调用
        :param driver: Appium驱动
        :return: True
        """
        driver.get_name('发现').click()
        driver.switch_h5()
        driver.get_classes('list-item')[1].click()
        driver.switch_app()
        driver.get_name('买入').click()
        username = self.cf.get('zjzh_login_info', 'username')
        password = self.cf.get('zjzh_login_info', 'password')
        if self.tra_login(username, password, driver):
            self.check_title(u'委托买入', driver)
            driver.back()
            driver.back()
            self.check_title(u'发现', driver)
            logging.info('资金账号登录成功')
            return True

    def tra_login(self, username, password, driver):
        """
        资金账号登录页面的登录方法
        :param username:账号
        :param password:密码
        :param driver:Appium驱动
        :return:True
        """
        driver.get_id('com.weizq:id/edit_account').clear()
        driver.get_id('com.weizq:id/edit_account').send_keys(username)
        logging.info('输入的账号为: {}'.format(username))
        driver.get_id('com.weizq:id/edit_password').send_keys(password)
        logging.info('输入的密码为: {}'.format(password))
        yzm = driver.get_id('com.weizq:id/text_yanzhengma').text
        logging.info('验证码为:{}'.format(yzm))
        driver.get_id('com.weizq:id/edit_yanzhengma').send_keys(yzm)
        driver.get_id('com.weizq:id/login').click()
        time.sleep(3)
        return True