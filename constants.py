class AppInfo:

    APPNAME = 'python-flist-client'
    APPVER = 0
    USERAGENT = APPNAME + '/' + str(APPVER)


class FlistEndpoints:

    """ https://toys.in.newtsin.space/api-docs/ """

    domain = "https://f-list.net"
    getApiTicket = "/json/getApiTicket.php"
    mappingList = "/json/api/mapping-list.php"
    characterData = "/json/api/character-data.php"
    characterFriends = "/json/api/character-friends.php"
    characterImages = "/json/api/character-images.php"
    characterMemoGet = "/json/api/character-memo-get.php"
    characterMemoSave = "/json/api/character-memo-save.php"
    characterGuestbook = "/json/api/character-guestbook.php"
    friendBookmarkLists = "/json/api/friend-bookmark-lists.php"
    bookmarkAdd = "/json/api/bookmark-add.php"
    bookmarkRemove = "/json/api/bookmark-remove.php"
    friendRemove = "/json/api/friend-remove.php"
    requestAccept = "/json/api/request-accept.php"
    requestDeny = "/json/api/request-deny.php"
    requestCancel = "/json/api/request-cancel.php"
    requestSend = "/json/api/request-send.php"
    # flist_reportSubmit = "/json/api/report-submit.php"
