all:
	${HOME}/Applications/hugo

clean:
	rm -fr public

publish:
	rsync -aOPvhe ssh --delete --exclude-from=/Users/harish/Scratch/Backup/exclude2 public/ ubuntu@harishnarayanan.org:/home/ubuntu/sites/harishnarayanan.org

checklinks:
	wget --spider -o wget.log -e robots=off -w 1 -r -p https://harishnarayanan.org/
