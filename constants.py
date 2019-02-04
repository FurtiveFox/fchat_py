class AppInfo:

    APPNAME = 'python-flist-client'
    APPVER = 0
    USERAGENT = APPNAME + '/' + str(APPVER)


class FlistEndpoints:

    """ https://toys.in.newtsin.space/api-docs/ """

    DOMAIN = "https://www.f-list.net"
    GETAPITICKET = "/json/getApiTicket.php"
    MAPPINGLIST = "/json/api/mapping-list.php"
    CHARACTERDATA = "/json/api/character-data.php"
    CHARACTERFRIENDS = "/json/api/character-friends.php"
    CHARACTERIMAGES = "/json/api/character-images.php"
    CHARACTERMEMOGET = "/json/api/character-memo-get.php"
    CHARACTERMEMOSAVE = "/json/api/character-memo-save.php"
    CHARACTERGUESTBOOK = "/json/api/character-guestbook.php"
    FRIENDBOOKMARKLISTS = "/json/api/friend-bookmark-lists.php"
    BOOKMARKADD = "/json/api/bookmark-add.php"
    BOOKMARKREMOVE = "/json/api/bookmark-remove.php"
    FRIENDREMOVE = "/json/api/friend-remove.php"
    REQUESTACCEPT = "/json/api/request-accept.php"
    REQUESTDENY = "/json/api/request-deny.php"
    REQUESTCANCEL = "/json/api/request-cancel.php"
    REQUESTSEND = "/json/api/request-send.php"
    # FLIST_REPORTSUBMIT = "/json/api/report-submit.php"
