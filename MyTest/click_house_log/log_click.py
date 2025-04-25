import logging
from colorama import init, Fore, Back, Style

# 初始化 colorama
init(autoreset=True)


# 自定义日志格式化器
class ColoredFormatter(logging.Formatter):
    # 定义不同日志等级对应的颜色
    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA
    }

    def format(self, record):
        # 获取日志等级对应的颜色
        log_color = self.COLORS.get(record.levelno, Fore.WHITE)
        # 定义日志格式
        format_str = '%(asctime)s - %(levelname)s - %(message)s'
        # 应用颜色到日志格式
        self._style._fmt = log_color + format_str + Style.RESET_ALL
        return super().format(record)

