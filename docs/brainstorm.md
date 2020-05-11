# Brainstorm.md
DATE: 05/07/2020


## Design goals

* Minimalist
* Able to be used as a module in future productivity apps that I make
* Features:
    * Add (non-recurring) events
    * Local, human readable file storage => You can manage your calendar in a text editor if you want
    * Simple (and written in python3), therefore hackable. Simplicity means there is no need for much abstraction.
    * Non-interactive environment to enable use in scripts.
    * Use MVC structure to allow for possibility of creating additional front-ends (like a basic android app)

## Implementation ideas

* Language: Python3
* Libraries and existing code bases:
     * arg-parse
     * python3 datetime module
     * python3 calendar module
* Commands correspond exactly to functions, option-flags correspond exactly to parameters. This allows for less abstraction and more hackability.
     


## Commands


### General usage

```sh

# General
scal [global-options] [command] [command-options] [command-args]


# Command usage
    add     ==> scal [global-options] add     [command-options::add-options]     [command-args::add-args]
    del     ==> scal [global-options] del     [command-options::del-options]     [command-args::del-args]
    edit    ==> scal [global-options] edit    [command-options::edit-options]    [command-args::edit-args]
    list    ==> scal [global-options] list    [command-options::list-options]    [command-args::list-args]
    getid   ==> scal [global-options] getid   [command-options::getid-options]   [command-args::getid-args]
    getname ==> scal [global-options] getname [command-options::getname-options] [command-args::getname-args]
    debug   ==> (for dev purposes only)
    

[global-options]
    --help        (-h)    ==> Prints help message (cannot be used with command)
    --verbose     (-v)    ==> Prints verbose output  # Not a priority
    --quiet       (-q)    ==> Prints quiet output  # NOT a priority
    no options or args    ==> Launches an interactive scal shell # not a priority
```

### add (command)

```sh

[add-options]
    --overwrite (-o) ==> If an item already exists with the same name, it will be deleted and overwritten with this entry
    --force     (-f) ==> If an item already exists with the same name, another item will be created with the name 
                         [item-name](n) where n is 2 for the second, 3 for the third, etc.


[add-args]
    [item-name] [start-time] [end-time] [notes]
    

[item-name]
    "item name" ==> Item names are unique. By default, if an item with the current name already exists, the 
                     command will be cancelled, and the user notified (unless another option is given)

[start-time] / [end-time]
    "yyyy-mm-dd day hh:mm" ==> Compatible with org-mode date/time entry
    
[notes]
    "Put any string here and they will be attached to the notes field of the item"

```


### del (command) RENAMED: `rm` -- to avoid python keyword collision

```sh

[del-options]
    TODO

[del-args]
    ( [item-name] | [itemID] )

[item-name]
    "item name"  ==> The name of the item. Item names are unique so it is unambiguous which to delete)


[itemID]
    n            ==> n is a python int that uniquely identifies an item. If the nth item is created in the 
                     calendar, then that item's itemID is n. Item ids are never recalculated, so item id's 
                     will continue to grow as the calendar is used.
```

### edit (command)

```sh

[edit-options]
    TODO

[edit-args]
    ( [item-name] | [itemID] ) attr1_name="attribute 1 name" ... attrN_name="attribute N name"  ==>
        Changes the specified attributes of the specified item.


[item-name]
    "item name"  ==> The name of the item. Item names are unique so it is unambiguous which to delete)


[itemID]
    n            ==> n is a python int that uniquely identifies an item. If the nth item is created in the 
                     calendar, then that item's itemID is n. Item ids are never recalculated, so item id's 
                     will continue to grow as the calendar is used.
```

### list (command)


```sh
[list-options]
    --verbose (-v)  ==>  Lists specified items and all of their attributes in an easy to read manner (default is verbose)
    --concise (-c)  ==>  Lists specified items and their essential info (Name, itemID, start-time, end-time) in a concise manner, one item per line)

[list-args]
    (
        :                        ==> List all items on this calendar
        yyyy-mm-dd               ==> List all items that start or end on this day
        yyyy-mm-dd:yyyy-mm-dd    ==> List all items that start or end on this interval
        yyyy-mm-dd:              ==> List all items that start or end on or after this day
        :yyyy-mm-dd              ==> List all items that start or end on or before this day
        ("Item name" | "itemID") ==> List the info for only the specified item
    )
```


### getid (command)

```sh

[getid-options] 
    TODO
    
[getid-args]
    "item name"  ==> Returns the id of the specified item


```


### getname (command)


```sh

[getname-options] 
    TODO
    
[getname-args]
    itemID  ==> Returns the name of the specified item


```



h
