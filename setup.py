import cx_Freeze

executables = [cx_Freeze.Executable(script="jogo.py", icon = "imagem.ico")]
cx_Freeze.setup(

    name= "jogo nave",
    options= {"build_exe":{

        "packages":["pygame"],
        "include_files":["E:\Jogo pronto"]

    }   },

    executables=executables

)

