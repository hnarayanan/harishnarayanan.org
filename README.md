# Here be dragons

This is an extreme work in progress, so be cautious about cloning this
code any time soon.

Also, this code at the moment is (c) Harish Narayanan 2015 **All
Rights Reserved**. So you probably shouldn't be pulling it anyway
since that doesn't give you much scope to do anything with it.

## TODO

The following list is in addition to the liberal `TODO`s sprinkled all
over the code.

- Expose RSS feed
- Every section needs a title and a description in some dictionary
- Replace the above non-license with something friendlier
- Replace this file with a useful README
- Grep for and remove all remaining egregious uses of inline styling
- Collect all article notes and make them draft posts
- Create archetypes for each primary content type on the site
- Incorporate some taxonomy for the articles (e.g. tags like Devops,
  Kubernetes, Django) to later start connecting up sets of articles
- Move in souped-up nginx configuration from the earlier repository
- Create a sister Ansible repository to setup the personal site?
- Reintroduce a meta section of the site... or perhaps move relevant
  information in this README and link to it?
- Incorporate online learning portfolio somewhere?
- Highlight recommended classes
- Add the winter in Asia gallery?
- Things I am playing with: Mesos, Kubernetes, Go, Containers and Swift-iOS


## Notes

rsync -aPvhe ssh --delete --exclude-from=/Users/harish/Scratch/Backup/exclude2 public/ ubuntu@harishnarayanan.org:/home/ubuntu/harishnarayanan.org
