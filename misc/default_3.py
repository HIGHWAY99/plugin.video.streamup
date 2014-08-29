### ############################################################################################################
###	#	
### # Site: 				#		
### # Author: 			#		The Highway
### # Description: 	#		
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc
import os,sys,string,StringIO,logging,random,array,time,datetime,re
try: import copy
except: pass
import urllib,urllib2,xbmcaddon,xbmcplugin,xbmcgui
import common as common
from common import *
from common import (_addon,_artIcon,_artFanart,_addonPath)
### ############################################################################################################
### ############################################################################################################
SiteName=ps('__plugin__')
SiteTag=ps('__plugin__').replace(' ','')
#mainSite=addst("site-domain")
#mainSite2='http://www.'+(mainSite.replace('http://',''))
mainSite="http://streamup.com"
mainSite2="https://streamup.com"
mainSite3="http://www.streamup.com"
mainSite4="https://www.streamup.com"
iconSite=_artIcon #'http://watchseries.lt/images/logo.png'
fanartSite=_artFanart
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan','13':'firebrick','14':'mediumpurple'}

CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyGenres=['Action','Adventure','Animation','Comedy','Drama','Family','Fantasy','Thriller','Reality TV','Sport','Sci-Fi','Documentary','Mystery','Talk Show','War','History','Crime','Music','Horror']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']
ww6='[COLOR black]@[/COLOR]'; 
ww7='[COLOR mediumpurple]@[/COLOR]'; 
colorA='FFFFFFFF'; colorB='FFAAAAAA'; colorC='FF777777'; 
workingUrl=mainSite+'ram.pls'
### ############################################################################################################
### ############################################################################################################
site=addpr('site','')
section=addpr('section','')
url=addpr('url','')
sections={'series':'series','movies':'movies'}
thumbnail=addpr('img','')
fanart=addpr('fanart','')
page=addpr('page','')
### ############################################################################################################
### ############################################################################################################
def About(head=''+cFL(SiteName,'blueviolet')+'',m=''):
	m=''
	if len(m)==0:
		m+='IRC Chat:  '+cFL('#XBMCHUB','blueviolet')+' @ '+cFL('irc.Freenode.net','blueviolet')
		m+=CR+'Site Name:  '+SiteName+CR+'Site Tag:  '+SiteTag+CR+'Site Domain:  '+mainSite+CR+'Site Icon:  '+iconSite+CR+'Site Fanart:  '+fanartSite
		m+=CR+'Age:  Please make sure you are of a valid age to watch the material shown.'
		#m+=CR+CR+'Known Hosts for Videos:  '
		#m+=CR+'* TrollVid'
		#m+=CR+'* UploadCrazy'
		m+=CR+CR+'Features:  '
		m+=CR+'* Browse Shows'
		m+=CR+'* Browse Episodes'
		m+=CR+'* Browse Host Links'
		m+=CR+'* Play Videos with UrlResolver'
		#m+=CR+'* Download Videos with UrlResolver'
		m+=CR+'* Optional MetaData where available.'
		#m+=CR+'* MetaData for Shows and 1st Season Episodes where data is available.'
		#m+=CR+'* MetaData auto-disabled for Anime List - ALL.  This is to prevent hammering with the huge list of nearly 400 shows.'
		m+=CR+CR+'Handled Sites:  '
		m+=CR+'* http://watchseries.lt'
		m+=CR+'* http://watchseries.sx'
		m+=CR+'* http://watchseries.ag'
		m+=CR+'* http://spainseries.lt (SPANISH)'
		m+=CR+'* http://watchseries.to'
		m+=CR+CR+'Notes:  '
		#m+=CR+'* '
		#m+=CR+'* '
		m+=CR+''
		m+=CR+ps('ReferalMsg')
		m+=CR+''
		m+=CR+''
		m+=CR+''
	import splash_highway as splash; splash.do_My_Splash(_addon.get_fanart(),5,False); 
	#splash.do_My_Splash(HowLong=5,resize=False); 
	#splash.do_My_Splash('http://i.imgur.com/tMKjZ6j.png',HowLong=5,resize=False); 
	
	String2TextBox(message=cFL(m,'cornflowerblue'),HeaderMessage=head)
	#RefreshList()
def spAfterSplit(t,ss):
	if ss in t: t=t.split(ss)[1]
	return t
def spBeforeSplit(t,ss):
	if ss in t: t=t.split(ss)[0]
	return t
def FixImage(img):
	#try: r1,r2=re.compile('(http://www.animefate.com/images/.+?)-\d+x\d+(\.[jpg|png|gif]+)').findall(img)[0]; img=r1+r2; 
	#except: pass
	return img
def AFColoring(t): 
	if len(t)==0: return t
	elif len(t)==1: return cFL(t,colorA) #colorA)
	else: return cFL(cFL_(t,colorA),colorB) #colorA),colorB)
def wwA(t,ww): #for Watched State Display
	if   ww==7: t=ww7+t
	elif ww==6: t=ww6+t
	return t

### ############################################################################################################
### ############################################################################################################
def psgn(x,t=".png"):
	s="http://i.imgur.com/"; d=artp('default_icon')
	try:
		return {
			'popular': 				artp('browse_popular') #d #s+""+t
			,'entertainment': artp('browse_entertainment') #d #s+""+t
			,'gaming': 				artp('browse_gaming') #d #s+""+t
			,'music': 				artp('browse_music') #d #s+""+t
			,'social': 				artp('browse_social') #artp('default_user') #d #s+""+t
			,'a': 		s+"OvFHLK2"+t
			,'b': 		s+"ezem9mn"+t
			,'c': 		s+"707ILz1"+t
			,'d': 		s+"BUT7dUz"+t
			,'e': 		s+"mzNtW2U"+t
			,'f': 		s+"11cykaC"+t
			,'g': 		s+"l0CvvHo"+t
			,'h': 		s+"VOupMGK"+t
			,'i': 		s+"ps3YPHq"+t
			,'j': 		s+"oNHwZWv"+t
			,'k': 		s+"TwHANG6"+t
			,'l': 		s+"xiuR2WX"+t
			,'m': 		s+"GDEAPud"+t
			,'n': 		s+"9FjSiMu"+t
			,'o': 		s+"TcR1pa0"+t
			,'p': 		s+"OGc4VBR"+t
			,'q': 		s+"hL9tEkx"+t
			,'r': 		s+"37NNHm8"+t
			,'s': 		s+"mFQswUE"+t
			,'t': 		s+"4DBQVrd"+t
			,'u': 		s+"qpovLUW"+t
			,'v': 		s+"bnu5ByY"+t
			,'w': 		s+"0IHoHV2"+t
			,'x': 		s+"ic81iKY"+t
			,'y': 		s+"46IlmRH"+t
			,'z': 		s+"PWUSCsE"+t
			,'0': 		s+"7an2n4W"+t # 0RJOmkw
			,'all': 	d #s+"hrWVT21"+t
			#,'search': 										s+"mDSHRJX"+t
			,'plugin settings': 					d #s+"K4OuZcD"+t
			,'local change log': 					d #s+"f1nvgAM"+t
			#,'last': 											s+"FelUdDz"+t
			#,'favorites': 								s+"lUAS5AU"+t
			#,'favorites 2': 							s+"EA49Lt3"+t
			#,'favorites 3': 							s+"lwJoUqT"+t
			#,'favorites 4': 							s+"Wr7GPTf"+t
			,'latest update': 						d #s+"dNCxQbg"+t
			,'completed': 								d #s+"xcqaTKI"+t
			#,'most popular': 							s+"T9LUsM2"+t
			#,'new anime': 								s+"BGZnMf5"+t
			#,'genre': 										s+"AmQHPvY"+t
			,'ongoing': 									d #s+"mBqFW3r"+t #EUak0Sg #ozEg86L
			,'anime list all': 						d #s+"t8b1hSX"+t
			,'anime list alphabet': 			d #s+"R0w0BAM"+t
			,'anime list latest update': 	d #s+"XG0LGQH"+t
			,'anime list newest': 				d #s+"eWAeuLG"+t
			,'anime list popularity': 		d #s+"eTrguP1"+t
			,'urlresolver settings': 			d #s+"PlROfSs"+t
			,'online bookmarks': 					d #s+"68ih1sx"+t
			#,'alphabetical': 							s+"sddCXQo"+t
			,'genre select': 							d #s+"MhNenb6"+t
#			,'': 								s+""+t
#			,'': 								s+""+t
			,'about': 										s+"8BLYGft"+t
			,'alphabetical': 							d #s+"aLKvpQD"+t
			,'favorites': 								d #s+"mVxogXL"+t #
			,'favorites 1': 							d #s+"cyDyVuh"+t #
			,'favorites 2': 							d #s+"GxH6BbM"+t #yRtrel2
			,'favorites 3': 							d #s+"Z9zKGJU"+t #
			,'favorites 4': 							d #s+"ovjBVu3"+t #
			,'favorites 5': 							d #s+"n8LUh2R"+t #
			,'favorites 6': 							d #s+"qN6FEit"+t #
			,'favorites 7': 							d #s+"3yQYXNh"+t #
			,'genre': 										d #s+"ObKUcJT"+t #XEIr4Cz
			,'icon': 											d #s+"VshtskV"+t
			,'fanart': 										d #s+"OSv7S2u"+t
			,'last': 											d #s+"3g6S9UH"+t
			,'latest episodes': 					d #s+"Skoe3Fm"+t #r19ycox
			,'latest updates': 						d #s+"E86Rnq5"+t
			,'most popular': 							d #s+"DzFexnz"+t #N69lo3G
			,'new anime': 								d #s+"wZN1olE"+t
			,'search': 										artp('default_channel') #s+"L8Ifj8L"+t #L8Ifj8L #MTnRQJ3
			,'search user': 							artp('default_user') #s+"L8Ifj8L"+t #MTnRQJ3
			,'random anime': 							d #s+"Rjag7b3"+t
			,'_': 												d #s+"bGMWifZ"+t
			,'anime 2013': 								d #s+"4SgqERs"+t
			,'anime 2014': 								d #s+"ijvRzvJ"+t
			,'anime 2015': 								d #s+"IYPai5I"+t
			,'anime 2016': 								d #s+"UqAYilt"+t
			,'anime list': 								d #s+"NTPFfwQ"+t
			,'a-z': 											d #s+"Br4ltnl"+t
			,'hot this season': 					d #s+"KcymQWL"+t
			,'latest animes': 						d #s+"mDFKTFN"+t
			,'movies': 										d #s+"hDYdtIr"+t
			,'random': 										d #s+"5uYkgTx"+t
			,'today': 										d #s+"GPxwlE8"+t
			,'tomorrow': 									d #s+"YX2EKk8"+t
			,'yesterday': 								d #s+"shqgyif"+t
#			,'': 								s+""+t
#			,'': 								s+""+t
#			,'': 								s+""+t
			,'img_next':									artp('browse_next') #d #'http://kissanime.com/Content/images/next.png'
			,'img_prev':									artp('browse_prev') #d #'http://kissanime.com/Content/images/previous.png'
			,'next':											artp('browse_next') #d #'http://kissanime.com/Content/images/next.png'
			,'prev':											artp('browse_prev') #d #'http://kissanime.com/Content/images/previous.png'
			###
#			,'': 								s+""+t
#			,'': 								s+""+t
#			,'': 								s+""+t
# KissAnimeGenres
# http://imgur.com/a/rws19/all
# http://imgur.com/a/rws19#Q12cars
# http://imgur.com/a/rws19
		}[x.lower()]
	except: 
		print 'failed to find graphc for %s' % (x); 
		return d
		#return ''
### ############################################################################################################
### ############################################################################################################
def PlayStreamUP(pageUrl='',Name='',Thumb='',roomId='',roomSlug='',plot='',liVe='',streamUrl='',streamkey='',youtubekey='',sourcetype='show'):
	PlayerMethod=addst("core-player"); url=''; print "--DO A PLAYER SPLIT HERE--"; debob(['pageUrl',pageUrl,'Name',Name,'Thumb',Thumb,'roomId',roomId,'roomSlug',roomSlug,'plot',plot,'liVe',liVe,'streamUrl',streamUrl]); 
	if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
	elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
	elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
	else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	play=xbmc.Player(PlayerMeth) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	#play=xbmc.Player(xbmc.PLAYER_CORE_AUTO) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	if len(streamUrl) > 10: url=streamUrl
	else: 
		html=messupText(nolines(nURL(pageUrl)),True,True); 
		if len(roomId)==0:
			try:    roomId=re.compile("flashvars.roomId\s*=\s*'(.+?)';").findall(html)[0]
			except: roomId=''
		if len(Thumb)==0:
			try:    Thumb=re.compile("flashvars.roomAvatar\s*=\s*'(.+?)';").findall(html)[0]
			except: Thumb=iconSite
		if len(roomSlug)==0:
			try:    roomSlug=re.compile("flashvars.roomSlug\s*=\s*'(.+?)';").findall(html)[0]
			except: roomSlug=''
		if len(Name)==0:
			try:    Name=re.compile("flashvars.roomName\s*=\s*'(.+?)';").findall(html)[0]
			except: Name='Unknown'
		## ### ## 
		## ### ## 
		## ### ## 
		NeedToToggleDebug=False; #NeedToToggleDebug=True; 
		if (len(url)==0) and (len(streamUrl)==0) and (len(streamkey)==0) and (len(youtubekey)==0):
				if NeedToToggleDebug==True: DoTD(); #DoA("ToggleDebug"); 
				url='rtmp://%s/%s' % ('66.55.92.79',roomId)
				play.play(url)
				xbmc.sleep(3000)
				if NeedToToggleDebug==True: DoTD(); #DoA("ToggleDebug"); 
				xbmcLogData=common._OpenFile(xbmcLogFile)
				if "--DO A PLAYER SPLIT HERE--" in xbmcLogData: xbmcLogData=xbmcLogData.split("--DO A PLAYER SPLIT HERE--")[-1]
				deb("test file",TPapp("-- player-test.txt")); 
				common._SaveFile(TPapp("-- player-test.txt"),xbmcLogData); 
				if "NetStream.Play.StreamNotFound" in xbmcLogData: deb("stream problem","could not find a stream."); 
				elif "STRING:	Failed to play ; stream not found." in xbmcLogData: deb("stream problem","failed to play, stream not found."); 
				try: sourcetype=re.compile('STRING:	{"message":"(.+?)"').findall(xbmcLogData)[-1]
				except: debob("no message found"); return
				deb("sourcetype",str(sourcetype));
				if (sourcetype.lower()=='startyoutubemode'): 
						debob('fetching youtubekey'); 
						try: youtubekey=re.compile('"message":"startYoutubeMode",.*"videoID":"(.+?)"').findall(xbmcLogData)[-1]
						except: debob("no youtubekey found"); return
						deb("youtubekey",youtubekey); 
				if (sourcetype.lower()=='startshowmode'):
						#try: streamkey=re.compile('INFO:\s+Property:\s+<Name:\s+.*?,\s+STRING:\s+{"message":"startShowMode","name":".*?","active":\D*,"streamKey":"([0-9A-Za-z]+)","uuid":".*?","type":"\D*"}>').findall(xbmcLogData)[-1]
						#try: streamkey=re.compile('"message":"startShowMode",.*"streamKey":"([0-9A-Za-z]+)"').findall(xbmcLogData)[-1]
						try: streamkey=re.compile('"message":"startShowMode",.*"streamKey":"(.+?)"').findall(xbmcLogData)[-1]
						except: pass
						deb('streamkey',streamkey); 
		if (sourcetype.lower()=='youtube') or (sourcetype.lower()=='startyoutubemode'):
				deb("youtubekey",youtubekey); 
				url='plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=%s' % (youtubekey)
				#url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % youtubekey
		elif (sourcetype.lower()=='') or (sourcetype.lower()=='auto') or (sourcetype.lower()=='show') or (sourcetype.lower()=='streamup') or (sourcetype.lower()=='rtmp') or (sourcetype.lower()=='startshowmode'):
				deb('streamkey',streamkey); 
				url='rtmp://%s/%s/%s' % ('66.55.92.79',roomId,streamkey)
		else: debob("unknown sourcetype and not enough info available."); return
		## ### ## 
	## ### ## 
	#try: _addon.resolve_url(url)
	#except: pass
	#try: play.play(url)
	#except: pass
	## ### ## 
	deb('stream url',str(url)); 
	infoLabels={"Studio":liVe,"ShowTitle":Name,"Title":Name,"cover_url":Thumb,'plot':plot}; 
	li=xbmcgui.ListItem(Name,iconImage=Thumb,thumbnailImage=Thumb); 
	li.setInfo(type="Video", infoLabels=infoLabels ); li.setProperty('IsPlayable', 'true'); 
	try: _addon.resolve_url(url)
	except: pass
	try: play.play(url, li)
	except:
		try: play.play(url)
		except: pass
	#logging().Logger().setLevel(30); 
	### ### ## 

def ListShows(Url,Page='',TyPE='js',idList='[]', csrfToken=''):
	if len(csrfToken)==0:
		maipageHtml=nURL('https://streamup.com/',cookie_file=CookFile,load_cookie=False,save_cookie=True)
		tokenParam='content="(.*?)" name="csrf-token"'
		csrfToken=re.compile(tokenParam).findall(maipageHtml)[0]
	## ### ## 
	debob(['Url',Url,'TyPE',TyPE])
	if len(idList)==0: idList='[]'
	if len(Page)==0: page=1
	else: page=int(Page)
	deb('page',str(page))
	if len(Url)==0: return
	if (not mainSite in Url) and (not mainSite2 in Url) and (not mainSite3 in Url) and (not mainSite4 in Url): 
		#Url=mainSite+Url
		Url=mainSite2+Url
	deb('Url',Url); 
	if (page==1) or (len(Page)==0): IdsList=[]; html=nURL(Url ,cookie_file=CookFile,load_cookie=False,save_cookie=True,headers={'X-CSRF-Token':csrfToken,'X-Requested-With':'XMLHttpRequest'}); 
	else: 
		##Url=Url.replace('http://','https://'); 
		IdsList=eval(idList); IdLa=0; iLISTd=''; IdsListZ=eval(idList);
		post_data={}
		post_data=[('already_loaded_rooms[]', i) for i in IdsList]
		print 'post_data',post_data
		for IdL in IdsList:
			#if IdLa==0: iLISTd+=' '; IdLa=1
			#if IdLa==0: iLISTd+='&'; IdLa=1
			if IdLa==0: iLISTd+=''; IdLa=1
			else: iLISTd+='&'
			iLISTd+=""+"already_loaded_rooms[]="+IdL+""
		#	#iLISTd+=""+"already_loaded_rooms[]="+IdL+"&"
		#	#iLISTd+=""+"already_loaded_rooms%5B%5D="+IdL+"&"
		## ### ## 
		UrlBB=Url +"?page="+str(page)+""#+str(iLISTd); 
		debob(['UrlBB',UrlBB]); 
		debob(['iLISTd',iLISTd]); 
		debob(['idList',idList]); 
		## ### ## 
		
		#html=nURL(UrlBB,method='post',form_data={'page':str(page),'already_loaded_rooms':str(idList)},headers={'Referer':Url},cookie_file=CookFile,load_cookie=True); 
		html=nURL(UrlBB,method='post',form_data=post_data,headers={'Referer':Url,'X-CSRF-Token':csrfToken,'X-Requested-With':'XMLHttpRequest','Origin': 'https://streamup.com','Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q='},cookie_file=CookFile,load_cookie=True,save_cookie=True)

		
		
		#html=nURL(UrlBB,method='post',form_data={'page':str(page),'already_loaded_rooms':str(idList)},headers={'Referer':Url}); 
		
		#html=nURL(UrlBB,method='post',form_data={'page':str(page),'already_loaded_rooms[]':str(iLISTd)},headers={'Referer':Url}); 
		#html=nURL(UrlBB,method='post',form_data={'page':str(page),'already_loaded_rooms[]':str(idList)},headers={'Referer':Url}); 
		#html=nURL(UrlBB,method='post',form_data={'page':str(page),'already_loaded_rooms':str(idList)},headers={'Referer':Url}); 
		#html=nURL(UrlBB,method='post',form_data={'page':str(page),'already_loaded_rooms':idList},headers={'Referer':Url}); 
		#html=nURL(UrlBB,method='post',form_data={'page':str(page),'already_loaded_rooms[]':str(idList)},headers={'Referer':Url}); 
		##html=nURL(UrlBB,method='post',form_data={'page':str(page),'already_loaded_rooms[]':str(idList),'already_loaded_rooms':str(idList)},headers={'Referer':Url}); 
		#html=nURL(UrlBB,method='post',form_data={'page':str(page),'already_loaded_rooms[]':str(idList)},headers={'Referer':Url}); 
		#html=nURL(UrlBB,method='post',form_data={'page':str(page),'already_loaded_rooms':str(idList)},headers={'Referer':Url}); 
		#html=nURL(UrlBB,method='post',form_data={'page':str(page),'already_loaded_rooms':str(idList)},headers={'Referer':Url}); 
		## ### ## 
		##html=nURL(Url,method='post',form_data={'page':str(page)},headers={'Referer':Url})
		##html=nURL(Url+"?page="+str(page)+"",method='post',form_data={'page':str(page),'already_loaded_rooms[]':str(idList),'already_loaded_rooms':str(idList)},headers={'Referer':Url})
		#html=nURL(Url+"?page="+str(page),method='post',form_data={'page':str(page),'already_loaded_rooms%5B%5D':str(idList)},headers={'Referer':Url})
		#html=nURL(Url+"?page="+str(page),method='post',form_data={'already_loaded_rooms[]':str(idList)},headers={'Referer':Url})
		#html=nURL(Url+"?page="+str(page),method='post',form_data=post_data:str(idList)},headers={'Referer':Url}

		#html=nURL(Url+"?page="+str(page),method='post',form_data={'page':str(page),'already_loaded_rooms':str(idList)},headers={'Referer':Url})
		##html=nURL(Url+"?page="+str(page)+""+str(iLISTd),method='post',form_data={'page':str(page),'already_loaded_rooms[]':str(idList),'already_loaded_rooms':str(idList)},headers={'Referer':Url})
		## ### ## 
	html=messupText(nolines(html),True,True); 
	deb('length of html',str(len(html))); #debob(html); 
	if len(html)==0: eod(); return
	if "<title>Offline for Maintenance</title>" in html: debob("Offline for Maintenance"); eod(); return
	html=html.replace('\\n','').replace('\n','').replace('\r','').replace('\a','').replace('\t','').replace("\\'","'").replace('\\"','"').replace('\\/','/')
	if TyPE=='xml':
		s="<a class='js-already-loaded-channel' data-room-id='(.*?)' data-room-slug='(.*?)' href='(.+?)'>"+"<div class='.*?'>(?:<div class='(homeChannel(?:Live|Title|Text)?)'>(.*?)</div>)?"+"<div class='(homeChannel(?:Live|Title|Text)?)'>(.*?)</div><div class='(homeChannel(?:Live|Title|Text)?)'>(.*?)</div>"+'<img alt="(.*?)(?: (\d+))?" onerror=".*?" src="(.*?)" /></div></a'; 
	elif TyPE=='js':
		s="<a class='js-already-loaded-channel' data-room-id='(.*?)' data-room-slug='(.*?)' href='(.+?)'>"+"<div class='.*?'>(?:<div class='(homeChannel(?:Live|Title|Text)?)'>(.*?)</div>)?"+"<div class='(homeChannel(?:Live|Title|Text)?)'>(.*?)</div><div class='(homeChannel(?:Live|Title|Text)?)'>(.*?)</div>"+'<img alt="(.*?)(?: (\d+))?" onerror=".*?" src="(.*?)" /></div></a'; 
	elif TyPE=='js|featured':
		s="<div class='homeChannelsFeatured-\d+' data-roomSlug='(.*?)'><div id='(homeChannelsFeaturedTextLabel)'>(Featured)</div><h2 id='(homeChannelsFeaturedTextChannelName)'>"+'<a href="(.+?)">(.+?)</a'; 
	elif TyPE=='html':
		s="<a class='js-already-loaded-channel' data-room-id='(.*?)' data-room-slug='(.*?)' href='(.+?)'>"+"<div class='.*?'>(?:<div class='(homeChannel(?:Live|Title|Text)?)'>(.*?)</div>)?"+"<div class='(homeChannel(?:Live|Title|Text)?)'>(.*?)</div><div class='(homeChannel(?:Live|Title|Text)?)'>(.*?)</div>"+'<img alt="(.*?)(?: (\d+))?" onerror=".*?" src="(.*?)" /></div></a'; 
		#s="<a class='js-already-loaded-channel' data-room-id='(.*?)' data-room-slug='(.*?)' href='(.+?)'>"+"<div class='.*?'><div class='homeChannelText'>(.*?)</div>"+"(?:<div class='homeChannelLive'>(.*?)</div>)?"+"<div class='homeChannelTitle'>(.*?)</div>"+'<img alt="(.*?)(?: (\d+))?" onerror=".*?" src="(.*?)" /></div></a'; 
		if 'users.js' in Url: 
			TyPE='html|user'; 
			#s="<a href='(.+?)'><div class='homePerson(?: homePerson\d+)?'><div class='homePersonText'>(.*?)</div><div class='homePersonUsername'>(.*?)</div>"+'<img alt="(.*?)" class="js-user-avatar-image" onerror=".*?" src="(.*?)" /></div></a'; 
			s="<a href='(.+?)'><div class='homePerson(?: homePerson\d+)?'><div class='(homePerson(?:Username|Text)?)'>(.*?)</div><div class='(homePerson(?:Username|Text)?)'>(.*?)</div>"+'<img alt="(.*?)" class="js-user-avatar-image" onerror=".*?" src="(.*?)" /></div></a'; 
	elif TyPE=='html|user':
		s="<a href='(.+?)'><div class='homePerson(?: homePerson\d+)?'><div class='(homePerson(?:Username|Text)?)'>(.*?)</div><div class='(homePerson(?:Username|Text)?)'>(.*?)</div>"+'<img alt="(.*?)" class="js-user-avatar-image" onerror=".*?" src="(.*?)" /></div></a'; 
	else: return
	html=html.replace('</a>','</a\n>'); ListOfIds=[]; 
	ListOfIds=IdsList
	debob(html); 
	try: matches=re.compile(s).findall(html); deb('# of matches found',str(len(matches))); debob(matches)
	except: matches=''; 
	if len(matches) > 0:
		#for (url,img,name,genres,status,NoEps,year) in matches:
		iC=len(matches); 
		for match in matches: #(img,url,name,genres)
			labs={}; cMI=[]; genres=''; Genres2=""; is_folder=False; 
			if TyPE=='html|user':
				#(url,name,img,liVe,plot,roomId,roomSlug)=(match[0],match[2],match[4],'',match[1],'',''); is_folder=True; 
				na=1; nnn=[[na,na+1],[na+2,na+3]]; (name,liVe,plot)=('','',''); is_folder=True; (roomId,roomSlug)=('',''); (url,img)=(match[0],match[6].replace('https://','http://')); 
				for (nb,nc) in nnn:
					if (len(name)==0) and (match[nb]=='homePersonUsername') and (len(match[nc]) > 0): name=match[nc]
					if (len(plot)==0) and (match[nb]=='homePersonText') and (len(match[nc]) > 0): plot=match[nc]
				#debob(['url',url,'name',name,'img',img,'plot',plot])
			elif TyPE=='js|featured':
				#s="<div class='homeChannelsFeatured-\d+' data-roomSlug='(.*?)'><div id='(homeChannelsFeaturedTextLabel)'>(Featured)</div><h2 id='(homeChannelsFeaturedTextChannelName)'>"+'<a href="(.+?)">(.+?)</a></h2>'; 
				na=1; nnn=[[na,na+1],[na+2,na+3]]; (name,liVe,plot)=(match[5],match[2],''); is_folder=True; 
				(roomId,roomSlug)=('',match[0]); (url,img)=(match[4],artp('default_channel')); 
				#for (nb,nc) in nnn:
				#	if (len(name)==0) and (match[nb]=='homePersonUsername') and (len(match[nc]) > 0): name=match[nc]
				#	if (len(plot)==0) and (match[nb]=='homePersonText') and (len(match[nc]) > 0): plot=match[nc]
				#debob(['url',url,'name',name,'img',img,'plot',plot])
			else:
				#(url,name,img,liVe,plot,roomId,roomSlug)=(match[2],match[5],match[8],match[4],match[3],match[0],match[1]); 
				na=3; nnn=[[na,na+1],[na+2,na+3],[na+4,na+5]]; (name,liVe,plot)=('','',''); (roomId,roomSlug,url,img)=(match[0],match[1],match[2],match[11].replace('https://','http://')); 
				for (nb,nc) in nnn:
					if (len(name)==0) and (match[nb]=='homeChannelTitle') and (len(match[nc]) > 0): name=match[nc]
					if (len(liVe)==0) and (match[nb]=='homeChannelLive') and (len(match[nc]) > 0): liVe=match[nc]
					if (len(plot)==0) and (match[nb]=='homeChannelText') and (len(match[nc]) > 0): plot=match[nc]
				#debob(['url',url,'name',name,'img',img,'liVe',liVe,'plot',plot])
				#(homeChannel(?:Live|Title|Text)?)
			#debob(['url',url,'name',name,'img',img])
			#(url,name)=(match[2],match[1])
			ListOfIds.append(roomId); #IdsList.append(roomId); 
			#name=name.replace('<span class="epnum">',' (').replace('</span>',')')
			
			#img=iconSite; #img=FixImage(img); 
			#img=img.replace(' ','%20'); 
			fimg=fanartSite; deb('img',img); 
			
			imgHtml=nURL(img,method='get',headers={'Referer':Url})
			#debob(['imgHtml',imgHtml])
			if len(imgHtml)==0: img=artp('default_channel')
			
			labs[u'plot']=plot; 
			if len(liVe) > 0: labs[u'title']=cFL(name+cFL(" ["+cFL(liVe,colorC)+"]",colorB),colorA); 
			else: labs[u'title']=cFL(name,colorA); 
			#plot+=CR+"Genres:  [COLOR purple]"+Genres2+"[/COLOR]"; #plot+="[CR]Year: [COLOR purple]"+year+"[/COLOR]"; #plot+="[CR]Status: [COLOR purple]"+status+"[/COLOR]"; #plot+="[CR]Number of Episodes: [COLOR purple]"+NoEps+"[/COLOR]"; 
			pars={'roomid':roomId,'roomslug':roomSlug,'url':url,'title':name,'fimg':fimg,'type':TyPE,'live':liVe,'imdb_id':'','img':img,'mode':'PlayStreamUP','site':site,'section':section,'sourcetype':'auto'}; 
			if TyPE=='html|user': pars['mode']='ListShows'; pars['page']=''; pars['type']='html'; 
			Clabs={'title':name,'year':'','url':url,'commonid':'','img':img,'fanart':fimg,'plot':labs[u'plot'],'todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}; 
			try: cMI=ContextMenu_Series(Clabs); 
			except: pass
			debob(['pars',pars,'labs',labs]); 
			try: _addon.add_directory(pars,labs,is_folder=is_folder,fanart=fimg,img=img,contextmenu_items=cMI,total_items=iC,context_replace=False)
			except: pass
	NextPage=str(int(page)+1); 
	if (("page="+NextPage) in html) and (not TyPE=='js|featured'):
		_addon.add_directory({'mode':'ListShows','site':site,'url':Url,'page':NextPage,'type':str(TyPE),'idlist':str(ListOfIds),'csrfToken':csrfToken},{'title':cFL('>> Next %s' % cFL(NextPage,colorA),colorB)},is_folder=True,fanart=fanartSite,img=psgn('next'))
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()

def Fav_List(site='',section='',subfav=''):
	debob(['test1',site,section,subfav]); 
	favs=fav__COMMON__list_fetcher(site=site,section=section,subfav=subfav); 
	ItemCount=len(favs); 
	debob('test2 - '+str(ItemCount)); 
	if len(favs)==0: myNote('Favorites','None Found'); eod(); return
	debob(favs); 
	favs=sorted(favs,key=lambda item: (item[0],item[1]),reverse=False); 
	for (_name,_year,_img,_fanart,_Country,_Url,_plot,_Genres,_site,_subfav,_section,_ToDoParams,_commonID,_commonID2) in favs:
		if _img > 0: img=_img
		else: img=iconSite
		if _fanart > 0: fimg=_fanart
		else: fimg=fanartSite
		debob('_ToDoParams'); debob(_ToDoParams)
		pars=_addon.parse_query(_ToDoParams)
		pars[u'fimg']=_fanart; pars[u'img']=_img; 
		#if len(_commonID) > 0: pars['imdb_id']=_commonID
		debob('pars'); debob(pars)
		_title=AFColoring(_name)
		if (len(_year) > 0) and (not _year=='0000'): _title+=cFL('  ('+cFL(_year,'mediumpurple')+')',colorA)
		if len(_Country) > 0: _title+=cFL('  ['+cFL(_Country,'mediumpurple')+']',colorA)
		wwT=_name+" ~~ "; 
		try:
			if visited_check2(wwT)==True: ww=7
			else: ww=6
		except: ww=6
		#try:
		if ww > 1:
			contextLabs={'title':_name,'year':_year,'img':_img,'fanart':_fanart,'country':_Country,'url':_Url,'plot':_plot,'genres':_Genres,'site':_site,'subfav':_subfav,'section':_section,'todoparams':_ToDoParams,'commonid':_commonID,'commonid2':_commonID2}
			##contextLabs={'title':_name,'year':'0000','url':_url,'img':img,'fanart':fimg,'DateAdded':'','todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}
			contextMenuItems=ContextMenu_Favorites(contextLabs)
			contextMenuItems.append( ('Empty List','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'mode':'cFavoritesEmpty','site':site,'section':section,'subfav':subfav}) ) )
			#contextMenuItems=[]
			_title=wwA(_title,ww); 
			_addon.add_directory(pars,{'title':_title,'plot':_plot},is_folder=True,fanart=fimg,img=img,total_items=ItemCount,contextmenu_items=contextMenuItems)
		#except: pass
		#
	#
	if 'movie' in section.lower(): content='movies'
	else: content='tvshows'
	set_view(content,view_mode=int(addst('tvshows-view'))); eod()


### ############################################################################################################
### ############################################################################################################
def DoSearch_Post(title='',Url='/search/results.php'):
	if len(Url)==0: return
	if mainSite not in Url: Url=mainSite+Url; 
	if len(title)==0: title=showkeyboard(txtMessage=title,txtHeader="Search:  ("+site+")")
	if (title=='') or (title=='none') or (title==None) or (title==False): return
	#deb('Searching for',title); title=title.replace('+','%2B').replace('&','%26').replace('?','%3F').replace(':','%3A').replace(',','%2C').replace('/','%2F').replace('=','%3D').replace('@','%40').replace(' ','+'); 
	deb('Searching for',title); #ListShows( Url+( title.replace(' ','+') ) ); 
	deb('Url',Url); html=messupText(nolines(nURL(Url,method='post',form_data={'search':title,'page':'','hidden_page':'','valider':'GO'})),True,True); deb('length of html',str(len(html))); #debob(html); 
	if len(html)==0: return
	ListShowsH(Url,html)
	##
def DoSearch(title='',Url='/search/'):
	if len(Url)==0: return
	if mainSite not in Url: Url=mainSite+Url; 
	if len(title)==0: title=showkeyboard(txtMessage=title,txtHeader="Search:  ("+site+")")
	if (title=='') or (title=='none') or (title==None) or (title==False): return
	deb('Searching for',title); title=title.replace('+','%2B').replace('&','%26').replace('?','%3F').replace(':','%3A').replace(',','%2C').replace('/','%2F').replace('=','%3D').replace('@','%40').replace(' ','%20'); 
	deb('Searching for',title); 
	##
	if ('_s_' in Url) or ('%s' in Url): Url=Url.replace('_s_','%s'); doUrl=Url % ( title.replace(' ','%20') )
	else: doUrl=Url + ( title.replace(' ','%20') )
	ListShows( doUrl ,'','html'  ); 
	##
def SpecialMenu(url):
	try: 
		if not '://' in url: html=common._OpenFile(TPapp(url))
		else: html=nURL(url)
		html=html.replace('\n','').replace('\r','').replace('\a','').replace('\t',''); data=eval(html); 
	except: data=[]
	iC=len(data); 
	if iC > 0:
		for (tag1,pars,tag2,labs) in data:
			img=pars['img'].replace('https://','http://'); fimg=pars['fimg'].replace('https://','http://'); 
			if fimg.lower()=='[fanart]': fimg=fanartSite
			debob(['pars',pars,'labs',labs]); 
			try: _addon.add_directory(pars,labs,is_folder=False,fanart=fimg,img=img,total_items=iC,context_replace=False)
			except: pass
	#set_view('list',view_mode=addst('default-view')); eod()
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()
	##
def DevFeaturedMenu():
	data=[]; 
	data.append(['pars', {'streamurl': 'rtmp://66.55.92.79/91813392-05eb-486c-ba35-588c3d83f194/6xz69ho3twFsdxSTn7LD', 'roomslug': 'scifi-and-stuff', 'site': '', 'imdb_id': '', 'fimg': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/backgrounds/000/011/044/original/scifi-and-stuff-background_1403478667.jpg?1403478667', 'img': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/avatars/000/011/044/cinematic/scifi-and-stuff_1407528717.jpg?1407528717', 'title': 'scifi and stuff', 'url': '/scifi-and-stuff', 'type': 'js', 'section': '', 'live': 'Live', 'mode': 'PlayStreamUP', 'roomid': '91813392-05eb-486c-ba35-588c3d83f194'}, 'labs', {u'plot': '', u'title': '[COLOR FFFFFFFF]scifi and stuff[COLOR FFAAAAAA] [[COLOR FF777777]Live[/COLOR]][/COLOR][/COLOR]'}])
	data.append(['pars', {'streamurl': 'rtmp://66.55.92.79/a39f295f-5d51-4ecc-a7a9-976753f54594/ryhNcYybmfogwszSuNKH', 'roomslug': 'wikids-sci-fi-network', 'site': '', 'imdb_id': '', 'fimg': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/backgrounds/000/011/846/original/wikids-sci-fi-network-background_1406776905.jpg?1406776905', 'img': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/avatars/000/011/846/cinematic/wikids-sci-fi-network_1407994668.jpg?1407994668', 'title': 'wikids sci-fi network', 'url': '/wikids-sci-fi-network', 'type': 'js', 'section': '', 'live': 'Live', 'mode': 'PlayStreamUP', 'roomid': 'a39f295f-5d51-4ecc-a7a9-976753f54594'}, 'labs', {u'plot': '', u'title': '[COLOR FFFFFFFF]wikids sci-fi network[COLOR FFAAAAAA] [[COLOR FF777777]Live[/COLOR]][/COLOR][/COLOR]'}])
	data.append(['pars', {'streamurl': 'rtmp://66.55.92.79/c7bedc20-0bfe-4c25-bcfc-87724433a0d2/veHUPayVdZwrAFw4dnFU', 'roomslug': 'liaoalan1', 'site': '', 'imdb_id': '', 'fimg': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/backgrounds/000/014/794/original/liaoalan1-background_1407508549.jpg?1407508549', 'img': 'https://d2f6rj4zotxt7y.cloudfront.net/rooms/avatars/000/014/794/cinematic/liaoalan1_1407507250.jpg?1407507250', 'title': 'liaoalan1', 'url': '/liaoalan1', 'type': 'html', 'section': '', 'live': 'Live', 'mode': 'PlayStreamUP', 'roomid': 'c7bedc20-0bfe-4c25-bcfc-87724433a0d2'}, 'labs', {u'plot': '', u'title': '[COLOR FFFFFFFF]liaoalan1[COLOR FFAAAAAA] [[COLOR FF777777]Live[/COLOR]][/COLOR][/COLOR]'}])
	#data.append()
	#data.append()
	#data.append()
	#data.append()
	#data.append()
	#data.append()
	iC=len(data)
	for (tag1,pars,tag2,labs) in data:
		img=pars['img']; fimg=pars['fimg']; #debob(['pars',pars,'labs',labs]); 
		try: _addon.add_directory(pars,labs,is_folder=False,fanart=fimg,img=img,total_items=iC,context_replace=False)
		except: pass
	#set_view('list',view_mode=addst('default-view')); eod()
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()
	##
def BrowseMenu():
	_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'popular','type':'js'},{'title':AFColoring('Popular')},is_folder=True,fanart=fanartSite,img=psgn('popular'))
	_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'entertainment','type':'js'},{'title':AFColoring('Entertainment')},is_folder=True,fanart=fanartSite,img=psgn('entertainment'))
	_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'gaming','type':'js'},{'title':AFColoring('Gaming')},is_folder=True,fanart=fanartSite,img=psgn('gaming'))
	_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'music','type':'js'},{'title':AFColoring('Music')},is_folder=True,fanart=fanartSite,img=psgn('music'))
	_addon.add_directory({'mode':'BrowseCat','site':site,'cat':'social','type':'js'},{'title':AFColoring('Social')},is_folder=True,fanart=fanartSite,img=psgn('social'))
	set_view('list',view_mode=addst('default-view')); eod()
	##
def SectionMenu():
	#import splash_highway as splash; #splash.do_My_Splash(_addon.get_fanart(),2,False); 
	#splash.do_My_Splash(HowLong=5,resize=False); 
	SpecialCODE=addst('special-code',''); LocalLists=[]; 
	_addon.add_directory({'mode':'BrowseMenu','site':site},{'title':AFColoring('Browse')},is_folder=True,fanart=fanartSite,img=psgn('browse'))
	_addon.add_directory({'mode':'SpecialMenu','url':'http://raw.github.com/HIGHWAY99/plugin.video.streamup/master/lists/DevsFeaturedList.txt','site':site},{'title':AFColoring("Dev's Featured List")},is_folder=True,fanart=fanartSite,img=psgn('browse'))
	
	LocalLists.append(['MyPicksList.txt','My Picks List','browse'])
	LocalLists.append(['LocalList.txt','Local List','browse'])
	#LocalLists.append(['','','browse'])
	for (urlA,TiTLE,iMg) in LocalLists:
		urlB=TPapp(urlA)
		if isFile(urlB)==True:
			html=common._OpenFile(urlB)
			if len(html) > 10:
				_addon.add_directory({'mode':'SpecialMenu','url':urlA,'site':site},{'title':AFColoring(TiTLE)},is_folder=True,fanart=fanartSite,img=psgn(iMg))
	
	if SpecialCODE==ps('special-code'):
		_addon.add_directory({'mode':'DevFeaturedMenu','site':site},{'title':AFColoring("Dev's Featured List[CR][Hard Coded]")},is_folder=True,fanart=fanartSite,img=psgn('browse'))
	
	_addon.add_directory({'mode':'BrowseCat2','site':site,'cat':'rooms','type':'js|featured'},{'title':AFColoring('Featured')},is_folder=True,fanart=fanartSite,img=psgn('browse'))
	_addon.add_directory({'mode':'Search','site':site,'url':'/search/'},{'title':AFColoring('Search')+cFL(' Channel',colorB)},is_folder=True,fanart=fanartSite,img=psgn('search'))
	_addon.add_directory({'mode':'Search','site':site,'url':'/search/_s_/users.js'},{'title':AFColoring('Search')+cFL(' People',colorB)},is_folder=True,fanart=fanartSite,img=psgn('search user'))
	#
	#if SpecialCODE==ps('special-code'):
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section             },{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.1.name'),colorB)},fanart=fanartSite,img=psgn('favorites 1'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'2'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.2.name'),colorB)},fanart=fanartSite,img=psgn('favorites 2'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'3'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.3.name'),colorB)},fanart=fanartSite,img=psgn('favorites 3'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'4'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.4.name'),colorB)},fanart=fanartSite,img=psgn('favorites 4'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'5'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.5.name'),colorB)},fanart=fanartSite,img=psgn('favorites 5'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'6'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.6.name'),colorB)},fanart=fanartSite,img=psgn('favorites 6'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'7'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.7.name'),colorB)},fanart=fanartSite,img=psgn('favorites 7'))
	###
	#if (len(addst("LastShowListedURL")) > 0): 
	#	pars={'site':site,'section':section,'mode':'ListEpisodes','url':addst("LastShowListedURL"),'title':addst("LastShowListedNAME"),'imdb_id':addst("LastShowListedIMDBID"),'img':addst("LastShowListedIMG"),'fimg':addst("LastShowListedFANART")}; 
	#	title=AFColoring(addst("LastShowListedNAME"))+CR+cFL('[Last Show]',colorA); 
	#	_addon.add_directory(pars,{'title':title},fanart=addst("LastShowListedFANART"),img=addst("LastShowListedIMG"),is_folder=True); 
	#if (len(addst("LastEpisodeListedURL")) > 0): 
	#	pars={'site':site,'section':section,'mode':'GetMedia','url':addst("LastEpisodeListedURL"),'title':addst("LastEpisodeListedNAME"),'imdb_id':addst("LastEpisodeListedIMDBID"),'img':addst("LastEpisodeListedIMG"),'fimg':addst("LastEpisodeListedFANART"),'stitle':addst("LastEpisodeListedSTITLE"),'etitle':addst("LastEpisodeListedETITLE"),'e':addst("LastEpisodeListedEpNo"),'s':addst("LastEpisodeListedSNo"),'e2':addst("LastEpisodeListedEpNo2")}; 
	#	title=AFColoring(addst("LastEpisodeListedNAME"))+CR+cFL('[Last Episode]',colorA); 
	#	_addon.add_directory(pars,{'title':title},fanart=addst("LastEpisodeListedFANART"),img=addst("LastEpisodeListedIMG"),is_folder=True); 
	###
	#_addon.add_directory({'mode':'About','site':site,'section':section},{'title':AFColoring('About')},is_folder=True,fanart=fanartSite,img='http://i.imgur.com/0h78x5V.png') # iconSite
	###
	set_view('list',view_mode=addst('default-view')); eod()
### ############################################################################################################
### ############################################################################################################
def mode_subcheck(mode='',site='',section='',url=''):
	if (mode=='SectionMenu'): 		SectionMenu()
	elif (mode=='') or (mode=='main') or (mode=='MainMenu'): SectionMenu()
	elif (mode=='SubMenu'): 			SubMenu()
	elif (mode=='SpecialMenu'): 	SpecialMenu(url)
	elif (mode=='DevFeaturedMenu'): 		DevFeaturedMenu()
	elif (mode=='BrowseMenu'): 					BrowseMenu()
	elif (mode=='ListShows'): 		ListShows(url,addpr('page',''),addpr('type',''),addpr('idlist',''),addpr('csrfToken',''))
	elif (mode=='BrowseCat'): 		ListShows("https://streamup.com/rooms/%s.js" % addpr('cat',''),addpr('page',''),addpr('type',''),addpr('idlist',''))
	elif (mode=='BrowseCat2'): 		ListShows("https://streamup.com/%s.js" % addpr('cat',''),addpr('page',''),addpr('type',''),addpr('idlist',''))
	elif (mode=='Search'):				DoSearch(addpr('title',''),url)
	elif (mode=='PlayStreamUP'): 				PlayStreamUP(url,addpr('subfav','title'),addpr('subfav','img'),addpr('roomid',''),addpr('roomslug',''),addpr('plot',''),addpr('live',''),addpr('streamurl',''),addpr('streamkey',''),addpr('youtubeid',''),addpr('sourcetype','show'))
	#
	elif (mode=='FavoritesList'): Fav_List(site=site,section=section,subfav=addpr('subfav',''))
	elif (mode=='About'): 				eod(); About()
	elif (mode=='PlayURL'): 						PlayURL(url)
	elif (mode=='PlayURLs'): 						PlayURLs(url)
	elif (mode=='PlayURLstrm'): 				PlayURLstrm(url)
	elif (mode=='PlayFromHost'): 				PlayFromHost(url)
	elif (mode=='PlayVideo'): 					PlayVideo(url)
	elif (mode=='PlayItCustom'): 				PlayItCustom(url,addpr('streamurl',''),addpr('img',''),addpr('title',''))
	elif (mode=='PlayItCustomL2A'): 		PlayItCustomL2A(url,addpr('streamurl',''),addpr('img',''),addpr('title',''))
	elif (mode=='Settings'): 						_addon.addon.openSettings() # Another method: _plugin.openSettings() ## Settings for this addon.
	elif (mode=='ResolverSettings'): 		import urlresolver; urlresolver.display_settings()  ## Settings for UrlResolver script.module.
	elif (mode=='ResolverUpdateHostFiles'):	import urlresolver; urlresolver.display_settings()  ## Settings for UrlResolver script.module.
	elif (mode=='TextBoxFile'): 				TextBox2().load_file(url,addpr('title','')); #eod()
	elif (mode=='TextBoxUrl'):  				TextBox2().load_url(url,addpr('title','')); #eod()
	elif (mode=='Download'): 						
		try: _addon.resolve_url(url)
		except: pass
		debob([url,addpr('destfile',''),addpr('destpath',''),str(tfalse(addpr('useResolver','true')))])
		DownloadThis(url,addpr('destfile',''),addpr('destpath',''),tfalse(addpr('useResolver','true')))
	elif (mode=='toJDownloader'): 			SendTo_JDownloader(url,tfalse(addpr('useResolver','true')))
	elif (mode=='cFavoritesEmpty'):  	fav__COMMON__empty( site=site,section=section,subfav=addpr('subfav','') ); xbmc.executebuiltin("XBMC.Container.Refresh"); 
	elif (mode=='cFavoritesRemove'):  fav__COMMON__remove( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year','') )
	elif (mode=='cFavoritesAdd'):  		fav__COMMON__add( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year',''),img=addpr('img',''),fanart=addpr('fanart',''),plot=addpr('plot',''),commonID=addpr('commonID',''),commonID2=addpr('commonID2',''),ToDoParams=addpr('todoparams',''),Country=addpr('country',''),Genres=addpr('genres',''),Url=url ) #,=addpr('',''),=addpr('','')
	elif (mode=='AddVisit'):							
		try: visited_add(addpr('title')); RefreshList(); 
		except: pass
	elif (mode=='RemoveVisit'):							
		try: visited_remove(addpr('title')); RefreshList(); 
		except: pass
	elif (mode=='EmptyVisit'):						
		try: visited_empty(); RefreshList(); 
		except: pass
	elif (mode=='refresh_meta'):			refresh_meta(addpr('video_type',''),addpr('title',''),addpr('imdb_id',''),addpr('alt_id',''),addpr('year',''))
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); import mMain
mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
