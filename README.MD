# Fake JSON Samples Generation Scripts. 
---
> Notice: Data generated from these scripts are generally fake. Should in case it reflects someone's private details, that's unintentional. A sample of this code is available in Golang and it is served over an API. 

Get placeholder samples for your projects using this mini scripts built in python.  
- - - 

## Samples Available. 
You can generate sample for your projects in regards to users data, posts, comments, todos and store products.

### Users 
Generate user samples.
Fields are selected at random. by default, you can get a result of 100 users at a time.
You can access user details on other sample files with their ID's.

User Fields
```
id, 
name, 
occupation,
photoURL,
age, 
dateOfBirth, 
maritalStatus,
gender,
countryOfOrigin, 
email, 
phoneLine, 
address:{
    street, 
    cordinates:{
        longitude, 
        latitude,
    }
}
```

### Todos
Generate placeholder Todo samples for you application. By default, you can access *30* todos. 

Todo Fields
```
id
activity, 
status,
userID, 
time

```

### Posts 
Generate placeholder Post Samples. By default *100* posts. 

Post Fields. 
```
title,
content,
userID,
photoURL,
postID,
datePosted

```

### Comments
Get Comments under a post with a specific postID. comments are picked from a sample of *80* comments

Comment Fields 
```
comment,
id,
postID, 
userID, 
datePosted, 

```