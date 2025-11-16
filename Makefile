all:
	hugo

clean:
	rm -fr public

publish:
	rsync -aOPvhe ssh --delete --exclude-from=.exclude public/ harish@metroplex:/var/www/harishnarayanan.org

install: publish

checklinks:
	wget --spider -o wget.log -e robots=off -w 1 -r -p https://harishnarayanan.org/
