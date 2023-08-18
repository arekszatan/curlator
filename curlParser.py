import logging


class CurlParser:

    def getTypeOfCurl(self, curl):
        if curl.find("&methodString") != -1:
            return 1
        elif curl.find("&callMethod") != -1:
            return 2
        else:
            logging.warning(f'Can not find type of {curl} !!!')
            return -1

    def getListOfParamForCurlMethodString(self, curl):
        curl = curl.split()[2]
        index = curl.find("&p=") + 3
        param = curl[index:]
        indexParam = param.find("'")
        param = param[:indexParam]
        return param

    def getListOfParamForCurlCallMethod(self, curl):
        tablicaParametrow = []
        index = curl.find("params") + 7
        for i in range(int(curl[index:index + 1])):
            index = curl.find(f'&p{i+1}=') + 4
            paramter = curl[index:]
            indexend = paramter.find("&")
            indexedn1 = paramter.find('http://')-2
            if indexend != -1:
                paramter = paramter[:indexend]
            else:
                paramter = paramter[:indexedn1]
            tablicaParametrow.append(paramter)
        return tablicaParametrow

    def createFinishCurlMethodString(self, curl, param):
        curlnew = curl[:curl.find("&p=") + 3]
        curlnew = curlnew + str(param[0]) + self.getEndofCurl(curl)

        if curlnew.find('https://') != -1:
            curlnew = curlnew + self.httpsCurl()
        return curlnew

    def createFinishCurlCallMethod(self, curl, param):
        if len(param) > 0:
            newCurl = curl[:curl.find("&p1")]
        else:
            newCurl = curl[:curl.find('" ')]
        i = 1
        for p in param:
            newCurl = newCurl + "&p" + str(i) + "=" + str(p)
            i += 1
        newCurl = newCurl + self.getEndofCurl(curl)

        if newCurl.find('https://') != -1:
           newCurl = newCurl + self.httpsCurl()

        return newCurl

    def getEndofCurl(self, curl):
        if curl.find('https://') != -1:
            curl = '" ' + curl.split()[-2]
            return str(curl)

        curl = '" ' + curl.split()[-1]
        return str(curl)

    def httpsCurl(self):
        end = ' -k'
        return end

