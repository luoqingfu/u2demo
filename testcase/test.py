import uiautomator2 as u2

d = u2.connect('5ea14c1f')
print(d.info)
#d.app_install('https://imtt.dd.qq.com/16891/7E569C80A3714D58E77F6173EB8F6329.apk?fsname=com.netease.cloudmusic_5.7.2_130.apk&csr=1bbd')

d.healthcheck()
d.app_start('com.netease.cloudmusic')
d(resourceId='com.netease.cloudmusic:id/aaq').click()