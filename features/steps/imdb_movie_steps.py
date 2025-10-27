from behave import given, when, then
from selenium import webdriver
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_results_page import ImdbResultsPage
from pages.imdb_movie_page import ImdbMoviePage

@given("el usuario está en el home page de imdb.com")
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")
    context.imdb_home = ImdbHomePage(context.driver)

@when('busca la pelicula "{movie_name}"')
def step_search_movie(context, movie_name):
    context.imdb_home.search_movie(movie_name)
    context.imdb_results = ImdbResultsPage(context.driver)

@when("el usuario selecciona el primer resultado")
def step_select_first_result(context):
    context.imdb_results.click_movie_link()
    context.imdb_movie = ImdbMoviePage(context.driver)

@then('el titulo de la pelicula debe ser "Origen"')
def step_get_movie_title(context):
    obtained_data = context.imdb_movie.get_movie_title()
    assert obtained_data == "Origen", f"El titulo de la pelicula no coincide: {obtained_data} != 'Origen'"


@then('la calificacion de la pelicula debe ser "8,8"')
def step_get_movie_review(context):
    obtained_data = context.imdb_movie.get_movie_review()
    assert obtained_data == "8,8", f"La calificacion de la pelicula no coincide: {obtained_data} != '8,8'"
    context.driver.quit()