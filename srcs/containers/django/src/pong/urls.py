from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('api/home/', views.home_view, name='api_home'),
	path('api/logout/', views.logout_view, name='logout'),

	path('api/game_mode/', views.game_mode_view, name='api_game_mode'),

	path('api/tournament/', views.tournament_view, name='api_tournament'),

	path('api/two_player/', views.two_player_view, name='api_two_player'),
	path('api/two_player_local/', views.two_player_local_view, name='api_two_player_local'),
	path('api/two_player_online/', views.two_player_online_view, name='api_two_player_online'),

	path('api/pong/', views.pong, name='api_pong'),
	path('api/tournament_score/', views.tournament_score, name='api_tournament_score'),
	path('api/create_tournament/', views.create_tournament, name='create_tournament'),
	path('api/add_participant/', views.add_participant, name='add_participant'),
	path('api/create_match/', views.create_match, name='create_match'),
	path('api/contract_address/', views.get_contract_address, name='get_contract_address'),
	path('api/register_matches/', views.register_matches, name='register_matches'),
	path('api/register_user/', views.load_page_reg, name='load_page'),
	path('api/login_user/', views.load_page, name='load_page_login'),
    path('api/register/', views.register, name='api-register'),
    path('api/login/', views.login, name='api-login'),
    path('api/userinfo/', views.userinfo_view, name='userinfo'),
    path('api/update-profile/', views.update_profile, name='userinfo'),
    path('api/update-profile-page/', views.load_page_update, name='userinfo'),
    
	# path('api/pong_solo/', views.pong_solo_view, name='api_pong_solo'),
	# path('api/pong_tournament/', views.pong_tournament_view, name='api_pong_tournament'),
	# path('api/pong_two_player_local/', views.pong_two_player_local_view, name='api_pong_two_player_local'),
	# path('api/pong_two_player_online/', views.pong_two_player_online_view, name='api_pong_two_player_online'),

]
