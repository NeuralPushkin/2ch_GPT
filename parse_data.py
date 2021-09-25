import api2ch
brds= ['b','d','sn','cc','soc','po','un','o','po']
ch = []
fieldnames = ['board','post','tags']
import csv
from tqdm import tqdm, trange
with open('2ch.csv', 'w', newline='') as csvfile:
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for b in brds:

          api = api2ch.DvachApi(b)

          board = api.get_board()
          pbar = tqdm(total=len(board))

          print(f'Total {len(board)} threads in {api.board.id}')
          for thread in board:
              #print(thread)
              pbar.update(1)
              try:
                thread = api.get_thread(thread)
                pbar1 = tqdm(total=len(thread))

                for post in thread:
                  pbar1.update(1)
                  #print(post.comment)
                  try:
                    comm = post.comment.split('</a><br>')[1]
                    tags = post.tags
                    writer.writerow({'board':b, 'post':comm,'tags':tags  })
                  except:
                    #print(post.comment)
                    writer.writerow({'board':b, 'post':post.comment,'tags':tags  })
                #ch+=[(thread.post.comment)]
                pbar1.close()
              except:
                  print('err')
          pbar.close()  
