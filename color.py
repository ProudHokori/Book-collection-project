class ConsoleColor:
    """ This class is used to decorate text on console """
    # method form
    header = '\033[95m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    italic = '\33[3m'
    curl = '\33[4m'
    blink = '\33[5m'
    selected = '\33[7m'

    # text color
    black = '\33[30m'
    red = '\33[31m'
    green = '\33[32m'
    yellow = '\33[33m'
    blue = '\33[34m'
    violet = '\33[35m'
    beige = '\33[36m'
    white = '\33[37m'

    # text background
    blackBG = '\33[40m'
    redBG = '\33[41m'
    greenBG = '\33[42m'
    yellowBG = '\33[43m'
    blueBG = '\33[44m'
    violetBG = '\33[45m'
    beigeBG = '\33[46m'
    whiteBG = '\33[47m'

    # text bold color
    greyB = '\33[90m'
    redB = '\33[91m'
    greenB = '\33[92m'
    yellowB = '\33[93m'
    blueB = '\33[94m'
    violetB = '\33[95m'
    beigeB = '\33[96m'
    whiteB = '\33[97m'
    cyanB = '\033[96m'

    # text highlight
    greyH = '\33[100m'
    redH = '\33[101m'
    greenH = '\33[102m'
    yellowH = '\33[103m'
    blueH = '\33[104m'
    violetH = '\33[105m'
    beigeH = '\33[106m'
    whiteH = '\33[107m'


class ScreenColor:
    """ This class is used to decorate color and picture on screen """
    # light theme
    baseScreen = '#FFF8F0'
    popupWindow = '#FEFEFF'
    mainText = '#827081'
    subText = '#9A8C98'
    decorate = '#7C7062'
    pointer = 'pointer.gif'

    # dark theme
    baseScreen2 = '#5E5A5A'
    popupWindow2 = '#767171'
    mainText2 = '#E8A6B1'
    subText2 = '#FEDBAC'
    decorate2 = '#F7E5EF'
    pointer2 = 'pointer2.gif'

    # mono theme
    baseScreen3 = '#D9D9D9'
    popupWindow3 = '#F2F2F2'
    mainText3 = '#595959'
    subText3 = '#7F7F7F'
    decorate3 = '#404040'
    pointer3 = 'pointer3.gif'

    # peach theme
    baseScreen4 = '#F8EDEC'
    popupWindow4 = '#FBF6F3'
    mainText4 = '#BD7D7F'
    subText4 = '#DDA8A7'
    decorate4 = '#A99F83'
    pointer4 = 'pointer4.gif'

    # winter theme
    baseScreen5 = '#D0D9E2'
    popupWindow5 = '#F2F2F2'
    mainText5 = '#527190'
    subText5 = '#8891B6'
    decorate5 = '#A5A5A5'
    pointer5 = 'pointer5.gif'

    # yaoi theme
    baseScreen6 = '#E9E4F0'
    popupWindow6 = '#FEF7F4'
    mainText6 = '#766B93'
    subText6 = '#B8A8D0'
    decorate6 = '#8D8AA5'
    pointer6 = 'pointer6.gif'

    # decorate picture
    picture = 'logo_app.gif'
    picture2 = 'yaoi.gif'

    def select_theme(self, theme='default'):
        """ Used to change theme color and pointer of app
        :param theme: string of theme name that user choose from app.py
        """
        if theme == 'dark':
            self.baseScreen = self.baseScreen2
            self.popupWindow = self.popupWindow2
            self.mainText = self.mainText2
            self.subText = self.subText2
            self.decorate = self.decorate2
            self.pointer = self.pointer2

        elif theme == 'mono':
            self.baseScreen = self.baseScreen3
            self.popupWindow = self.popupWindow3
            self.mainText = self.mainText3
            self.subText = self.subText3
            self.decorate = self.decorate3
            self.pointer = self.pointer3

        elif theme == 'peach':
            self.baseScreen = self.baseScreen4
            self.popupWindow = self.popupWindow4
            self.mainText = self.mainText4
            self.subText = self.subText4
            self.decorate = self.decorate4
            self.pointer = self.pointer4

        elif theme == 'winter':
            self.baseScreen = self.baseScreen5
            self.popupWindow = self.popupWindow5
            self.mainText = self.mainText5
            self.subText = self.subText5
            self.decorate = self.decorate5
            self.pointer = self.pointer5

        elif theme == 'yaoi':
            self.baseScreen = self.baseScreen6
            self.popupWindow = self.popupWindow6
            self.mainText = self.mainText6
            self.subText = self.subText6
            self.decorate = self.decorate6
            self.pointer = self.pointer6
            self.picture = self.picture2
