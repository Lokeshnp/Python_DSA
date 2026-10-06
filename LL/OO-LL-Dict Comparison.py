# Head                                      Tail
#  ↓                                          ↓
# [ 10 | ● ]  ─────→  [ 20 | ● ]  ─────→  [ 30 | NULL ]
#  Node 1              Node 2                  Node 3


head= {
        "value": 10,
         "next": { 
                    "value": 20,
                    "next": { 
                                "value": 30,
                                "next": None

                  } 
               
    }    
  
}

print(head['next']['next']['value'])

# print(my_linked_list.next.next.value)


