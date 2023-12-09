@echo off
title Titanium - Intro
color 0a
@echo # # # # # # # # # # # # # # # # # # #
@echo #                                   #
@echo #      Titanium Spy Builder         #
@echo #                                   #
@echo #   Installation In Progress...     #
@echo #                                   #
@echo # # # # # # # # # # # # # # # # # # #
@echo

title Titanium - Installation
color 0a
pip install -r requirements.txt
cls

title Titanium - Builder
color 0a
python builder.py
cls
