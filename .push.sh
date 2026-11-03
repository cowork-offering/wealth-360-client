#!/bin/bash
# Publish: archy holds the repo; Banksy holds the GitHub credential. Copy, then push from Banksy.
set -e
rsync -az --delete --exclude .push.sh /opt/connectry/projects/wealth-360-client/ ubuntu@98.87.86.133:~/wealth-360-client/
ssh -o BatchMode=yes ubuntu@98.87.86.133 'cd ~/wealth-360-client && (git remote get-url origin >/dev/null 2>&1 || git remote add origin https://github.com/cowork-offering/wealth-360-client.git) && git push origin main 2>&1 | tail -1'
