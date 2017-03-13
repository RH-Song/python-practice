try :
    file = open('fuck.txt','r+')
except Exception as e:
    print e
    print 'Done!'
    response = raw_input('Want a new file? ')
    print response
    if response == "y":
        file = open('fuck.txt','w')
        file.close()
    else :
        pass
else :
    file.write('ssss')
    file.close()
