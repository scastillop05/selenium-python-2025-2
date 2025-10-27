from behave import given, when, then
from selenium import webdriver
from pages.lastfm_home_page import LastFmHomePage
from pages.lastfm_results_page import ResultsPage
from pages.lastfm_artist_page import LastFmArtistPage

@given("el usuario está en el home page de last.fm")
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.last.fm/")
    context.lastfm_home = LastFmHomePage(context.driver)

@when('busca al artista "{artist_name}"')
def step_search_artist(context, artist_name):
    context.lastfm_home.search_artist(artist_name)
    context.lastfm_results = ResultsPage(context.driver)

@when("selecciona el primer resultado")
def step_select_result(context):
    context.lastfm_results.click_artist_link()
    context.lastfm_artist = LastFmArtistPage(context.driver)

@then('la fecha del ultimo release debe ser "{release_date}"')
def step_get_release_date(context, release_date):
    obtained_data = context.lastfm_artist.get_latest_release_date()
    assert obtained_data == release_date, f"Las fechas del ultimo releease del artista no coinciden: {obtained_data} != {release_date}"


