import logging
from common import project_path


class MyLog:
    def my_log(self, msg, level):
        # 定义一个日志收集器my——logger
        my_logger = logging.getLogger("python")

        # 设定级别
        my_logger.setLevel("DEBUG")
        # 设置日志输出格式
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%Y%b%d-%H:%M:%S")

        # 创建一个自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)
        # 输出到文本
        fh = logging.FileHandler(project_path.test_log_path, encoding="utf-8")
        fh.setLevel("DEBUG")  # 指定要输出日志的级别
        fh.setFormatter(formatter)

        # 两者对接--指定输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        elif level == "CRITICAL":
            my_logger.critical(msg)

        # 关闭渠道，不然日志会重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, "DEBUG")

    def info(self, msg):
        self.my_log(msg, "INFO")

    def warning(self, msg):
        self.my_log(msg, "WARNING")

    def error(self, msg):
        self.my_log(msg, "ERROR")

    def critical(self, msg):
        self.my_log(msg, "CRITICAL")


if __name__ == '__main__':
    pass
