#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.ThinkPHP import ThinkPHPArbitraryCommandExecutionVulnerability
from Modules.Cms.ThinkPHP import ThinkPHPArbitraryCommandExecutionVulnerability2
from Modules.Cms.ThinkPHP import ThinkPHPArbitraryCommandExecutionVulnerability3
from Modules.Cms.ThinkPHP import ThinkPHPSqlInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(ThinkPHPArbitraryCommandExecutionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(ThinkPHPArbitraryCommandExecutionVulnerability2.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(ThinkPHPArbitraryCommandExecutionVulnerability3.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(ThinkPHPSqlInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("ThinkPHP")