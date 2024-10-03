import logging
from typing import Optional, List, Union

from playwright.sync_api import Playwright, Browser, Page

from ..cfgloader import AppCfg
from . import constants

def get_browser(appcfg: AppCfg, playwright: Playwright) -> Optional[Browser]:
   if playwright is None:
      mylogger.debug('No playwright')
      return None
   
   mylogger = logging.getLogger(__name__)

   is_headless = False
   if appcfg.get(constants.CFG_KEY_HEADLESS_MODE) and appcfg.get(constants.CFG_KEY_HEADLESS_MODE).lower() == 'true':
      is_headless = True

   cfg_value = appcfg.get(constants.CFG_KEY_BROWSER_TYPE)
   if cfg_value and cfg_value.lower() == 'chrome':
      mylogger.debug('Chrome type browser return')
      return playwright.chromium.launch(headless=is_headless)
   elif cfg_value and cfg_value.lower() == 'firefox':
      mylogger.debug('Firefox type browser return')
      return playwright.firefox.launch(headless=is_headless)
   elif cfg_value and cfg_value.lower() == 'webkit':
      mylogger.debug('Webkit type browser return')
      return playwright.webkit.launch(headless=is_headless)
   
   mylogger.debug('No playwright return')
   return None