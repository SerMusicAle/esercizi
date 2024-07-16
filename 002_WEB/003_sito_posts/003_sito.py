"""
costruzione di un sito
    Costruire una pagina html fatta di:
        un body dove il css impone il testo centrato
        nel body mettere una griglia (grid layout di bootstrap)
        le colonne della griglia sono delle card .                        
        Dividere la pagina html in tre blocchi, chiamati pag11 pag12 pag13 in modo che valga la seguente relazione pag = pag11 + N*pag12 + pag13. 
        Per costruire i tre blocchi tenere conto di quanto discusso in classe. 
        Creare un semplice script in python che, assegnato un numero ad N, es. N = 3 genera la pagina html. 
"""

class Costruzione_sito ():
#INIT
    def __init__(self, titolo: str, menu_top:list[str], posts:str):
        
        #PATH
        self.file_path_html = "html/index.html"
        self.file_path_css = "syle.css"
        
        #DATI
        self.__titolo = titolo
        self.__posts = posts
        self.__menu_top = menu_top
        self.__posts_quantity: int = 0

    
    def f_menu_top(self):
        return ''.join(self.__menu_top)
    
    def f_posts(self):
        self.__posts_quantity: int = 12
        posts = ""
        for _ in range (self.__posts_quantity):
            posts += self.__posts  
        
        return posts 
    
    def f_structure(self):
        self.section_head = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{self.__titolo}</title>
                <link rel="stylesheet" href="../css/style2.css">
                <link rel="stylesheet" href="../css/bootstrap.min.css">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            </head>
            
            <body>
                <center>
                    <div class="header">
                        <div class="logo">Facedog</div>
                        <div class="user-menu">
                        
<!--SPOSTARE QUI IL MENU IN FUTURO SE SERVE-->

                        </div>
                    </div>
                    
                    <div class="top-menu">
                        {self.f_menu_top()}  
                    </div>
                    
                    <div class="main-content">

                        <div class="sidebar">
                            <div class="icon"><i class="fas fa-home-alt"></i></div>
                        </div>
                        

                        <div class="posts">
                            <div class="row">
                                {self.f_posts()}
                            </div>
                        </div>
                    </div>
                </center>
            </body>
            </html>
        """
        return self.section_head
    
    def f_costruttore(self):
        with open(self.file_path_html, 'w') as file:
            file.write(self.f_structure())
        print(f"file generato correttamente all'indirizzo {self.file_path_html}")
            
titolo: str = "Facedog"
menu_top: list[str] = [
            '<div class="icon"><i class= "fa fa-home"> Home</i></div>\n',
            '<div class="icon"><i class= "fa fa-search"> Search</i></div>\n',
            '<div class="icon"><i class= "fa fa-bell"> Bell</i></div>\n',
            '<div class="icon"><i class= "fa fa-envelope"> Envelope</i></div>\n',
            '<div class="icon"><i class= "fa fa-user"> User</i></div>\n'
        ]
posts: str = """
    <div class="col-sm-4">
        <div class="card">
            <img class="card-img-top" src="../img/dog.avif" alt="Card image cap" >
            <div class="card-body">
                <h5 class="card-title">Andiamo a spassoooooooo</h5>
                <p class="card-text">La grande storia di un animale che viaggiava per le city</p>
                <a href="#" class="btn btn-primary">Partiamooo</a>
            </div>
        </div>
    </div>  
"""       

if __name__ == "__main__":
    sito = Costruzione_sito (titolo, menu_top, posts)
    sito.f_costruttore()