git clone https://github.com/gauthamk02/TerminalHunt.git   -clones the repo in local file
mkdir solution -creates a directory
cd solution - opens a directory
cat >part1.txt  -"cat >" creates and then writes into a new file
107 ^d  -writes in the file
cd ..  -goes back to parent directory
cd 06
cat 1.txt >> part2.txt
cd ..
cp 06/1.txt solution  -"cp" copies a file
git log  -shows the log
cp 10/1.txt  solution
mv solution/1.txt  solution/part3.txt  -"mv" can be used for both moving a file and renaming a file
git remote add origin 'https://github.com/TejasMG12/amfoss-tasks' -now pushing the work to main repo
git add . 
git commit -m '..'
git push add origin main
git branch -a  -shows all the branches
git checkout asia  -opens a branch
name athens.txt  - finds a branch
git checkout main
git merge asia
cp Greek/athens.txt solution
mv solution/athens.txt  solution/part4.txt
cd solution
cat part1.txt part2.txt part3.txt part4.txt >>password.txt
rm part1.txt  
git add .
git commit '..'
git push add origin main
