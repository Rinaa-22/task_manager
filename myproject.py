import json
import argparse
from pathlib import Path
from colorama import Fore , Style , init
init(autoreset=True)


the_file = Path("project_task.json")

def loading ():
    '''when we have the project_task.json" , read the content and return it as a py list 
    else empty list '''
    if the_file.exists() :
        return json.loads(the_file.read_text())
    return []

def saving(jobs):
    ''' get a list of works and save it in project_task.json'''
    the_file.write_text(
        json.dumps(jobs, indent=2 ))

def adding(title , priority = 'medium') :
    jobs = loading()
    jobs.append({'title' : title , 'done' : False , 'priority' : priority})
    saving(jobs)
    print ( f" we added : {title}") 

def list_jobs(filter_type = None):
    jobs= loading()
    if filter_type == "pending" :
        jobs = [job for job in jobs if not job["done"]]
    elif filter_type == "done":
        jobs = [job for job in jobs if job["done"]]

    if not jobs :
        print("no jobs yet :)")
        return
    jobs.sort(key=lambda job : job["done"])
    for i , job in enumerate(jobs ,1):
       if job['done']:
           color = Fore.GREEN
           sign = 'x'
       else : 
           color = Fore.YELLOW
           sign = ' '
       priority_tag = f"({job['priority']})"
       print (color+f" [{sign}] {i}- {job['title']}{priority_tag}" + Style.RESET_ALL)

    done_count = sum( 1 for job in jobs if job["done"] )
    print( Fore.CYAN + f"{done_count}/{len(jobs)} jobs done" + Style.RESET_ALL)

def mark_done (index):
    """mark a job as done by its number""" 
    jobs = loading()
    if index <  1 or index > len(jobs) :
        print(" O_O ! invalid job number " )
        return
    jobs[index-1]['done'] = True
    saving(jobs)
    print (f"Marked as done job :{jobs[index -1]['title']}")

def removing(index):
    """remove a job by its number"""
    jobs = loading()
    if index <  1 or index > len(jobs) :
            print(" O_O ! invalid job number " )
            return
    removed = jobs.pop(index -1)
    saving(jobs)
    print (f"we removed {removed['title']}")

def search_jobs (keyword):
    jobs = loading()
    fits = [job for job in jobs if keyword.lower() in job["title"].lower()]
    if not fits :
        print(f"we don't have {keyword} , in our plan")
        return
    for i , job in enumerate (fits ,1):
        sign = "x" if job["done"] else " "
        color = Fore.GREEN if  job["done"] else Fore.YELLOW
        priority_tag = f"({job['priority']})"
        print (color + f" [{sign}] {i}- {job['title']} {priority_tag} " + Style.RESET_ALL)

def Help_me():
    print(Fore.CYAN + "*** Job Manager Help ***" + Style.RESET_ALL)
    print ()
    print("   add <title> [--priority high/medium/low ]    ")
    print("       Add a job ")
    print ()
    print("   list [--pending | --done ]    ")
    print("       show all the jobs and filters    ")
    print ()
    print("   done<number>  ")
    print("       mark a job as done    ")
    print ()
    print("   remove<number>  ")
    print("       Remove a job  ")
    print ()
    print("   search<keyword>  ")
    print("       search the job with their title  ")
    print ()
    print ("for example :")
    print('  python myproject.py add "learn python"--priority high  ')
    print('  python myproject.py list --pending')

def main_function( ):
    parser = argparse.ArgumentParser (description = 'Simple Jobs Manager')
    parser.add_argument("command" ,choices=['add' ,'done', 'list' , 'remove' , 'search','help'])
    parser.add_argument('value' , nargs='?')
    parser.add_argument("--priority" , choices = ["low","medium" ,"high"], default= "medium")
    parser.add_argument("--pending",action ="store_true")
    parser.add_argument("--done" , action="store_true")
    args = parser.parse_args()

    if args.command == 'add' :
        if args.value is None:
            print("Erorr : OOPs ! Please provide a job title first")
            return
        adding(args.value , args.priority)
        
    elif  args.command == 'list':
        if args.pending :
            list_jobs("pending")
        elif args.done:
            list_jobs("done")
        else  :
            list_jobs()


    elif args.command == "done":
        if args.value is None:
            print("Erorr : Oops! please provide a job number first ")
            return 
        try:
            mark_done(int(args.value))
        except ValueError :
            print("The job number should be integeer")


    elif args.command == "search":
        if args.value is None:
            print("Erorr : Oops! please provide a keyword first ")
            return  
        search_jobs(args.value)  

    elif args.command == "help":
        Help_me() 


    elif args.command == "remove" :
        if args.value is None:
            print("Erorr : Oops! please provide a job number first ")
            return
        try:
           removing(int(args.value))
        except ValueError :
            print("The job number should be integeer")      


if __name__ == "__main__"  :
    main_function()      
         
