all:
	/Users/harish/Desktop/new-personal-site/hugo

clean:
	rm -fr public

publish:
	rsync -aPvhe ssh --delete --exclude-from=/Users/harish/Scratch/Backup/exclude2 public/ ubuntu@harishnarayanan.org:/home/ubuntu/harishnarayanan.org
