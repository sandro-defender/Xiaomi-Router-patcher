#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Language translations for menu system
# Supported languages: en (English), zh (Chinese), ru (Russian)
# Repository translated to English - all display strings are in English

TRANSLATIONS = {
    'en': {
        'title': 'Xiaomi MiR Patcher',
        'main_menu': [
            'Set IP-address (current value: {})',
            'Connect to device (install exploit)',
            'Read full device info',
            'Create full backup',
            'Install EN/RU/ZH languages',
            'Install permanent SSH',
            'Install firmware (from directory "firmware")',
            '{{{ Other functions }}}',
            'Change language',
            '[[ Reboot device ]]',
            'Exit'
        ],
        'extended_menu': [
            'Set IP-address (current value: {})',
            'Change root password',
            'Read dmesg and syslog',
            'Create a backup of the specified partition',
            'Uninstall EN/RU/ZH languages',
            'Set kernel boot address',
            'Install bootloader (Breed/U-Boot)',
            '__test__',
            '[[ Reboot device ]]',
            'Return to main menu'
        ],
        'prompts': {
            'select': 'Select: ',
            'choice': 'Choice: ',
            'enter_ip': 'Enter device IP-address: ',
            'extended_functions': '(extended functions)',
            'language_menu': 'Language',
            'language_prompt': 'Select language [1-English, 2-Chinese, 3-Russian]: ',
            'bootloader_choice': 'Select bootloader [1-Breed, 2-U-Boot]: '
        },
        'messages': {
            'firmware_downgrade_title': 'FIRMWARE DOWNGRADE SUGGESTION:',
            'firmware_downgrade_be3600': 'If exploits are not working on your BE3600 router, please\ndowngrade to firmware version 1.0.68 or older.',
            'firmware_downgrade_rd15': 'RD15 (BE3600 2.5G) latest firmware v1.0.68 has fixed the vulnerability.\nPlease downgrade to v1.0.65 or older.',
            'firmware_downgrade_rd16': 'RD16 (BE3600 1G) latest firmware v1.0.40 has fixed the vulnerability.\nPlease downgrade to v1.0.34 or older.',
            'firmware_downgrade_tutorial': 'Firmware downgrade tutorial:\nhttps://github.com/uyez/lyq/releases/tag/be3600',
            'firmware_downgrade_tool': 'You can use the Xiaomi Router Repair Tool for downgrade.',
            'exploit_failed_title': 'EXPLOIT FAILED:',
            'exploit_failed_message': 'All available exploits failed to work on this device.\nThis may be due to newer firmware versions that have\npatched the vulnerabilities.',
            'exploit_failed_suggestion': 'Consider checking for alternative firmware versions\nor contact the community for device-specific solutions.'
        }
    },
    'zh': {
        'title': 'Xiaomi MiR Patcher',
        'main_menu': [
            'Set IP-address (current value: {})',
            'Connect to device (install exploit)',
            'Read full device info',
            'Create full backup',
            'Install EN/RU/ZH languages',
            'Install permanent SSH',
            'Install firmware (from directory "firmware")',
            '{{{ Other functions }}}',
            'Change language',
            '[[ Reboot device ]]',
            'Exit'
        ],
        'extended_menu': [
            'Set IP-address (current value: {})',
            'Change root password',
            'Read dmesg and syslog',
            'Create a backup of the specified partition',
            'Uninstall EN/RU/ZH languages',
            'Set kernel boot address',
            'Install bootloader (Breed/U-Boot)',
            '__test__',
            '[[ Reboot device ]]',
            'Return to main menu'
        ],
        'prompts': {
            'select': 'Select: ',
            'choice': 'Choice: ',
            'enter_ip': 'Enter device IP-address: ',
            'extended_functions': '(extended functions)',
            'language_menu': 'Language',
            'language_prompt': 'Select language [1-English, 2-Chinese, 3-Russian]: ',
            'bootloader_choice': 'Select bootloader [1-Breed, 2-U-Boot]: '
        },
        'messages': {
            'firmware_downgrade_title': 'FIRMWARE DOWNGRADE SUGGESTION:',
            'firmware_downgrade_be3600': 'If exploits are not working on your BE3600 router, please\ndowngrade to firmware version 1.0.68 or older.',
            'firmware_downgrade_rd15': 'RD15 (BE3600 2.5G) latest firmware v1.0.68 has fixed the vulnerability.\nPlease downgrade to v1.0.65 or older.',
            'firmware_downgrade_rd16': 'RD16 (BE3600 1G) latest firmware v1.0.40 has fixed the vulnerability.\nPlease downgrade to v1.0.34 or older.',
            'firmware_downgrade_tutorial': 'Firmware downgrade tutorial:\nhttps://github.com/uyez/lyq/releases/tag/be3600',
            'firmware_downgrade_tool': 'You can use the Xiaomi Router Repair Tool for downgrade.',
            'exploit_failed_title': 'EXPLOIT FAILED:',
            'exploit_failed_message': 'All available exploits failed to work on this device.\nThis may be due to newer firmware versions that have\npatched the vulnerabilities.',
            'exploit_failed_suggestion': 'Consider checking for alternative firmware versions\nor contact the community for device-specific solutions.'
        }
    },
    'ru': {
        'title': 'Xiaomi MiR Patcher',
        'main_menu': [
            'Set IP-address (current value: {})',
            'Connect to device (install exploit)',
            'Read full device info',
            'Create full backup',
            'Install EN/RU/ZH languages',
            'Install permanent SSH',
            'Install firmware (from directory "firmware")',
            '{{{ Other functions }}}',
            'Change language',
            '[[ Reboot device ]]',
            'Exit'
        ],
        'extended_menu': [
            'Set IP-address (current value: {})',
            'Change root password',
            'Read dmesg and syslog',
            'Create a backup of the specified partition',
            'Uninstall EN/RU/ZH languages',
            'Set kernel boot address',
            'Install bootloader (Breed/U-Boot)',
            '__test__',
            '[[ Reboot device ]]',
            'Return to main menu'
        ],
        'prompts': {
            'select': 'Select: ',
            'choice': 'Choice: ',
            'enter_ip': 'Enter device IP-address: ',
            'extended_functions': '(extended functions)',
            'language_menu': 'Language',
            'language_prompt': 'Select language [1-English, 2-Chinese, 3-Russian]: ',
            'bootloader_choice': 'Select bootloader [1-Breed, 2-U-Boot]: '
        },
        'messages': {
            'firmware_downgrade_title': 'FIRMWARE DOWNGRADE SUGGESTION:',
            'firmware_downgrade_be3600': 'If exploits are not working on your BE3600 router, please\ndowngrade to firmware version 1.0.68 or older.',
            'firmware_downgrade_rd15': 'RD15 (BE3600 2.5G) latest firmware v1.0.68 has fixed the vulnerability.\nPlease downgrade to v1.0.65 or older.',
            'firmware_downgrade_rd16': 'RD16 (BE3600 1G) latest firmware v1.0.40 has fixed the vulnerability.\nPlease downgrade to v1.0.34 or older.',
            'firmware_downgrade_tutorial': 'Firmware downgrade tutorial:\nhttps://github.com/uyez/lyq/releases/tag/be3600',
            'firmware_downgrade_tool': 'You can use the Xiaomi Router Repair Tool for downgrade.',
            'exploit_failed_title': 'EXPLOIT FAILED:',
            'exploit_failed_message': 'All available exploits failed to work on this device.\nThis may be due to newer firmware versions that have\npatched the vulnerabilities.',
            'exploit_failed_suggestion': 'Consider checking for alternative firmware versions\nor contact the community for device-specific solutions.'
        }
    }
}

def get_translation(lang, key, subkey=None, *args):
    """Get translated text for given language and key"""
    if lang not in TRANSLATIONS:
        lang = 'en'  # fallback to English
    
    trans = TRANSLATIONS[lang]
    
    # Handle nested dictionary lookup
    if subkey:
        if key in trans and isinstance(trans[key], dict) and subkey in trans[key]:
            text = trans[key][subkey]
            if args:
                return text.format(*args)
            return text
        # fallback to English
        elif lang != 'en' and key in TRANSLATIONS['en'] and isinstance(TRANSLATIONS['en'][key], dict) and subkey in TRANSLATIONS['en'][key]:
            text = TRANSLATIONS['en'][key][subkey]
            if args:
                return text.format(*args)
            return text
        else:
            return f"{key}.{subkey}"  # fallback key
    
    # Handle normal key lookup
    if key in trans:
        if isinstance(trans[key], list):
            return trans[key]
        elif args:
            return trans[key].format(*args)
        else:
            return trans[key]
    elif key in trans.get('prompts', {}):
        text = trans['prompts'][key]
        if args:
            return text.format(*args)
        return text
    else:
        # fallback to English only if we're not already using English
        if lang != 'en':
            return get_translation('en', key, subkey, *args)
        else:
            # If key not found even in English, return a default message
            if subkey:
                return f"[Missing translation: {key}.{subkey}]"
            else:
                return f"[Missing translation: {key}]"

def get_supported_languages():
    """Get list of supported language codes"""
    return list(TRANSLATIONS.keys())
