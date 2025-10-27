Feature: Buscar un artista y validar la fecha del ultimo release
    Scenario: Validar la fecha del ultimo lanzamiento de Bruno Mars
        Given el usuario está en el home page de last.fm
        When busca al artista "Bruno Mars"
        And selecciona el primer resultado
        Then la fecha del ultimo release debe ser "3 October 2025"