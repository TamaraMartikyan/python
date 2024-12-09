import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def filteredPosts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        posts = response.json()
        filtered_titles = [post for post in posts if len(post['title'].split()) <= 6]
        filtered_bodies = [post for post in filtered_titles if post['body'].count('\n') <= 3]
        return filtered_bodies
    else:
        print("GET request failed:", response.status_code)
        return []

def createPost():
    new_post = {
        "title": "A New Post",
        "body": "This is a simple body for testing.",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    if response.status_code == 201:
        return response.json()
    else:
        print("POST request failed:", response.status_code)
        return None

def updatePost(post_id):
    updated_post = {
        "title": "Updated Post Title",
        "body": "This is the updated content.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_post)
    if response.status_code == 200:
        return response.json()
    else:
        print("PUT request failed:", response.status_code)
        return None

def deletePost(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        return f"Post {post_id} deleted successfully."
    else:
        print("DELETE request failed:", response.status_code)
        return None


if __name__ == "__main__":

    print(" Filtered posts: ")
    filtered_posts = filteredPosts()
    for post in filteredPosts:
        print(post)

    print("\nCreating a new post ")
    created_post = createPost()
    if created_post:
        print(created_post)

    if created_post:
        print("\nUpdating the created post: ")
        updated_post = updatePost(created_post["id"])
        if updated_post:
            print(updated_post)

    if created_post:
        print("\nDeleting the created post: ")
        delete_message = deletePost(created_post["id"])
        if delete_message:
            print(delete_message)
