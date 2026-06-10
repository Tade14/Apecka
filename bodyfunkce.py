points = [10,20,30,36,50]
def soucet(body):
    body = 0
    for point in points:#projde nam to cely list a vezme tu hodntu a da to do points
        body += point
    return body
print(f"Celkove skore je:{soucet(points)}")
    
    

   