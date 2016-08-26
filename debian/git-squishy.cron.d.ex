#
# Regular cron jobs for the git-squishy package
#
0 4	* * *	root	[ -x /usr/bin/git-squishy_maintenance ] && /usr/bin/git-squishy_maintenance
