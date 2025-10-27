Feature: Buscar una pelicula y validar el titulo y la calificacion
    Scenario: Validar el titulo de la pelicula Inception y la calificacion
        Given el usuario está en el home page de imdb.com
        When busca la pelicula "Inception"
        And el usuario selecciona el primer resultado
        Then el titulo de la pelicula debe ser "Origen"
        And la calificacion de la pelicula debe ser "8,8"