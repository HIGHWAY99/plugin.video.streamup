### ############################################################################################################
###	#	
### # Author: 			#		The Highway
### # Description: 	#		Config File For:  The Binary Highway
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs
import os,sys,string,StringIO,logging,random,array,time,datetime,re
#from t0mm0.common.addon import Addon
#try: 		from t0mm0.common.addon 				import Addon
#except: 
#	try: from c_t0mm0_common_addon 				import Addon
#	except: pass
try: 			from addon.common.addon 				import Addon
except:
	try: 		from t0mm0.common.addon 				import Addon
	except: 
		try: from c_t0mm0_common_addon 				import Addon
		except: pass
### Plugin Settings ###
def ps(x):
	if (x=='_addon_id') or (x=='addon_id') or (x=='_plugin_id') or (x=='plugin_id'): return 'plugin.video.streamup'
	try: 
		return {
			'__plugin__': 					"StreamUP"
			,'__authors__': 				"[COLOR white]The[COLOR tan]Highway[/COLOR][/COLOR]"
			,'__credits__': 				""
			,'_domain_url': 				""
			,'word': 								""
			,'word0': 							""
			,'word1': 							""
			,'word2': 							""
			,'word3': 							""
			,'word4': 							""
			,'word5': 							""
			,'word6': 							""
			,'word7': 							""
			,'word8': 							""
			,'word9': 							""
			,'content_movies': 			"movies"
			,'content_tvshows': 		"tvshows"
			,'content_seasons': 		"seasons"
			,'content_episodes': 		"episodes"
			,'content_links': 			"list"
			,'default_section': 					'anime'
			,'section.wallpaper':					'wallpapers'
			,'section.tv': 								'tv'
			,'section.movies': 						'movies'
			,'section.anime': 						'anime'
			,'section.animesub': 					''
			,'section.animedub': 					''
			,'section.animesubmovies': 		''
			,'section.animesubseries': 		''
			,'section.animedubmovies': 		''
			,'section.animedubseries': 		''
			,'section.anime': 						''
			,'sep': 								os.sep
			,'special.home': 				'special:'+os.sep+os.sep+'home'
			,'special.home.addons': 'special:'+os.sep+os.sep+'home'+os.sep+'addons'+os.sep
			,'_addon_path_art': 		"art"
			,'_database_name': 			"animefate"
			,'default_art_ext': 		'.png'
			,'default_cFL_color': 	'cornflowerblue'
			,'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
			,'cMI.showinfo.url': 							'XBMC.Action(Info)'
			,'cMI.jDownloader.addlink.url':		'XBMC.RunPlugin(plugin://plugin.program.jdownloader/?action=addlink&url=%s)'
			,'filemarker': ''
			,'iiHubIrc': 'http://i.imgur.com/V3jly5Y.png' # #XBMCHUB IRC chat.freenode.net/6667 - Transperant
			,'fiHubIrc': 'http://i.imgur.com/UtL1F8j.png' # #XBMCHUB IRC chat.freenode.net/6667
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'ii': '' # 
			#,'fi': '' # 
			#,'': ''
			,'ReferalMsg': 'My XBMC-HUB Refferal Code - http://www.xbmchub.com/forums/register.php?referrerid=15468  [CR]Please use it to register if you don\'t have an account.  It not\'s not much but it can help me out.  '
			,'WhatRFavsCalled': 'Favs: '
		}[x]
	except: return ''







### ############################################################################################################
### ############################################################################################################
