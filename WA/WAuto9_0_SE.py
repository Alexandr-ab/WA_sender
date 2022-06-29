from time import sleep
from datetime import datetime
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# get the start datetime for a backup file
CURRENTTIME = datetime.now().strftime('%d-%m-%y(%H-%M)')

# import phone numbers from a file to a list, check in the sent base for a repetitions and write back in propriet format
def importAndSortPhoneNums(numFile, sentFile):
    repetitiveCount = 0
    uniqueCount = 0
    inputList = []
    with open(numFile, 'r') as inputFile, open(sentFile, 'r') as sentBase:
        sentList = [line.strip('\n') for line in sentBase]
        for line in inputFile:
            tempNumber = line.strip('\n')
            listNumber = ''.join([i for i in tempNumber if i.isdigit()])
            if listNumber not in inputList and listNumber not in sentList:
                if listNumber:
                    inputList.append(listNumber)
                    uniqueCount += 1
            else:
                repetitiveCount += 1
    print(f'Repetitive Numbers: {repetitiveCount}')
    print(f'Unique Numbers: {uniqueCount}')

    with open(numFile, 'w') as outputFile:
        [(outputFile.write(number + '\n')) if number != inputList[-1]
         else outputFile.write(number) for number in inputList]

    return inputList

# read the message from a file, and write it in a list
def getMessage(messageFile):
    messageList = []
    lineBreak = (Keys.CONTROL, Keys.ENTER)
    with open(messageFile, 'r', encoding='utf-8') as message:
        for line in message:
            # strip the default line breaks to avoid sending the message and add ctrl+enter to go to a new line
            messageList.append(line.strip('\n'))
            messageList.append(lineBreak)
    return messageList

# add used number to the sent base
def makeSentBase(sentFile, inputList):
    with open(sentFile, 'a') as sentBase:
        sentBase.write(inputList[0] + '\n')

# delete used numbers and backup
def delAndBackUp(outputFile, inputList):
    with open(outputFile, 'w') as output, open(f'{CURRENTTIME}_Phones_copy.txt', 'w') as backup:
        [(output.write(number + '\n'), backup.write(number + '\n')) if number != inputList[-1]
         else (output.write(number), backup.write(number)) for number in inputList]

def sendMessage(inputList, messageList, browser, sentBase, phoneFile):
    # add counters
    sent = 0
    notSent = 0
    delCounter = 0
    if browser == 'FF':
        driver = wd.Firefox()
    elif browser == 'Ch':
        driver = wd.Chrome()
    elif browser == 'Edge':
        driver = wd.Edge()
    # Open WA page and wait until QR-code will be scanned
    driver.get('https://web.whatsapp.com/')
    WebDriverWait(driver, 300).until(ES.presence_of_element_located((By.CSS_SELECTOR, '._1Flk2')))

    while True:  # sending cycle
        if len(inputList) <= 0:
            break
        # add the second loop to load the same number if have some trouble with loading
        while True:
            driver.get(f'https://web.whatsapp.com/send?phone={inputList[0]}')
            # use an exception if the page doesn't completely load
            try:
                # use lambda func to check both elements at the same time
                WebDriverWait(driver, 30).until(lambda driver: driver.find_elements_by_css_selector('._3NCh_')
                                                    or driver.find_elements_by_css_selector('footer ._2_1wd'))
                # if one of the elem is presented - use an exceptions to check if the number is incorrect or isn't
                # register in WA
                # check if it's window 'No internet' or 'Incorrect number'
                if driver.find_elements_by_css_selector('._1dwBj.Spzqc'):  # additional button on 'No internet' window
                    continue
                else:
                    # sending cycle
                    try:
                        sleep(1)  # delay until the element will be loaded
                        inputText = driver.find_element_by_css_selector('footer ._2_1wd')
                        [inputText.send_keys(i) for i in messageList]
                        inputText.send_keys(Keys.ENTER)
                        sleep(1)  # delay while the message is being sent
                        sent += 1
                        print(f'Sent: {inputList[0]} - {sent}')
                        break
                    except NoSuchElementException:
                        notSent += 1
                        print(f'Wrong Number: {inputList[0]}, Not Sent - {notSent}')
                        break
            # repeat the cycle with the same number if the page wasn't completely load
            except TimeoutException:
                continue

        # add number to the sent base
        makeSentBase(sentBase, inputList)
        # delete used number from the list and every 10 used numbers from the file and make backup file
        delCounter += 1
        del inputList[0]
        if delCounter >= 10:
            delCounter = 0
            delAndBackUp(phoneFile, inputList)
    driver.quit()

def fullProgram( browser='Ch', messageFile='message.txt', sourceFile='Phones.txt', sentBase='sent.txt'):  # browser = 'FF' / 'Ch' / 'Edge'
    inputList = importAndSortPhoneNums(sourceFile, sentBase)
    message = getMessage(messageFile)
    sendMessage(inputList, message, browser, sentBase, sourceFile)

fullProgram()
