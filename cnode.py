from selenium import webdriver
import unittest
import time
import HTMLTestRunner
import csv

class Register(unittest.TestCase):
        def setUp(self):
            self.driver=webdriver.Chrome()
            self.driver.get("http://118.31.19.120:3000/signup/")
            self.driver.maximize_window()

        def test_regis(self):
            my_file='./data.csv'
            data=csv.reader(open(my_file,'r'))
            for i in data:
                print(i[4])
                username="loginname"
                pwd="pass"
                repwd="re_pass"
                email="email"
                click="span-primary"
                info='//*[@id="content"]//strong'
                self.driver.find_element_by_id(username).send_keys(i[0])
                self.driver.find_element_by_id(pwd).send_keys(i[1])
                self.driver.find_element_by_id(repwd).send_keys(i[2])
                self.driver.find_element_by_id(email).send_keys(i[3])
                self.driver.find_element_by_class_name(click).click()
                time.sleep(5)
                print('\n' + '测试项：' + i[4])
                message=self.driver.find_element_by_xpath(info).text
                self.driver.get_screenshot_as_file('./picture/'+i[5]+".png")
                try:
                    self.assertEqual(message,i[6])
                    print('提示信息正确，预期值与实际值一致:')
                    print('预期提示:'+ i[6])
                    print('实际提示:'+ message)
                except:
                    print('提示信息错误，预期值与实际值不符：')
                    print('预期提示:'+ i[6])
                    print('实际提示:'+ message)
                self.driver.back()
                self.driver.refresh()

        def tearDown(self):
            self.driver.close()

testunit=unittest.TestSuite()
testunit.addTest(Register("test_regis"))
filepath='F:\\report.html'
fp=open(filepath,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='登陆-测试报告',description='测试执行情况')
runner.run(testunit)
fp.close()