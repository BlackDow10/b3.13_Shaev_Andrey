class Tag:
    def __init__(self, tag, text, is_single=False, **kwargs):
        self.tag = tag
        self.text = text
        self.attributes = kwargs
        self.is_single = is_single
        self.children = []
        
            

    def get(self):
        result = []
        firstPart = "<{} ".format(self.tag)
        itribut = ""
        for attr, val in self.attributes.items():
            if attr == "klass":
                attr = "class"
            itribut += '{}="{}" '.format(attr, val)
        itribut += ">"
        firstPart += itribut
        endPart = "</{}>\n".format(self.tag)
        result.append(firstPart)
        result.append(self.text + "\n")
        for child in self.children:
            result.append(child.get())
        if self.is_single == False:
            result.append(endPart)
        return result 
    
   

class HTML:
    def __init__(self, output = False):
        self.output = output
        self.children = []
        self.i = 0
        self.result = []
        

    
    def __str__(self):
        if self.output:
            with open("index.html", "w") as file:
                file.write("<html>\n")
                file.write(self.textForm(self.result))
                file.write("</html>")
                return("file was writen")
        else:
            stroka = "<html>\n"
            stroka += self.textForm(self.result)
            stroka += "<html>"
            return stroka

    def get(self):
        for child in self.children:
            self.result.append(child.get())
    
    def textForm(self, children):
        text = ""
        i = 0 
        while i < len(children):
            if type(children[i])==list:
                self.i +=4
                text +=self.textForm(children[i])
                self.i -=4
            else: 
                if i == 0 or i == (len(children) - 1):
                    text +=  " "*self.i + children[i]
                else:
                    text += children[i]
            i += 1 
        return text
    #определяет куда выводить данные

class TopLevelTag:
    def __init__(self, tag, text = "", **kwargs):
        self.tag = tag
        self.text = ""
        self.attributes = kwargs
        self.children = []
   
    def get(self):
        result = []
        firstPart = "<{} ".format(self.tag)
        itribut = ""
        for attr, val in self.attributes.items():
            if attr == "klass":
                attr = "class"
            itribut += '{}="{}" '.format(attr, val)
        itribut += ">"
        firstPart += itribut
        endPart = "</{}>\n".format(self.tag)
        result.append(firstPart)
        result.append(self.text + "\n")
        for child in self.children:
            result.append(child.get())
        result.append(endPart)
        return result 


"""Как работает:
Каждый тэг преобразуется в список. 
Тэг более низкого  уровня становится списком внутри списка.
Класс HTML преобразовывает список с вложенными списками в строки, задавая отступ в зависимости "как глубоко вложен список)))"

Как работать:
создаётся объект класса HTML , передаётся парамтр True если результат надо сохранить в файл, ничего не передаётся- если вывести на экран.
Далее создаются объекты head и body, которые принадлежат классу TopLevelTag. Передаются аргументы: tag- название тэга и text - текст. 
остальные параметры по типу: параметр = "значение"

Потом создаются тэги более низкого уровня. Передаются аргументы: tag- название тэга и text - текст, is_single = True  если тэг одиночный.
остальные параметры по типу: параметр = "значение"

далее тэги более низкого уровня добавляем к тэгам более высокого уровня в массив children

перед выводом выполняем метод get() в объекте html
и выполняем коменду принт(html)
Колличество вкладываемых тэгов не ограничено.
Выполнил Шаев Андрей.
"""
head = TopLevelTag(tag="head")
head.children.append(Tag(tag="title", text="заголовок", klass="text-align-right", id="heading-text"))
html = HTML()

body =  TopLevelTag(tag="body", text="dfgbdrfthbdrfthb")

zagolovok  = Tag(tag="h1", text="Заголовок", klass="text-align-right", id="heading-text", data_bind="not-above")
zagolovok.children.append(Tag(tag="p", text="Какой-то текст к заголовку...", klass="text", id="heading-text"))
body.children.append(zagolovok)

zagolovok  = Tag(tag="h3", text="Ещё Заголовок", klass="text-align-right", id="heading-text", data_bind="not-above")
zagolovok.children.append(Tag(tag="p", text="Какой-то текст к  ещё заголовку...", klass="text", id="heading-text"))
body.children.append(zagolovok)

html.children.append(head)   
html.children.append(body)
html.get()
print(html)