---
layout: post
title: "Post name here"
authornamehere: authornamehere
---

The purpose of authornamehere in the front matter (the --- variables --- part) is so Jenkins can differentiate between different people's posts and only print the appropriate posts on each blog. For example if Honor wants to make a post, she should make a copy of this template in \_posts/Honor and change the variable 'authornamehere' to 'Honor'. It is irrelevant what the value of the variable is; as long as the variable has a defined value, the post will appear on Honor's blog page.

All post content should be below the front matter. Note that currently, all blog layouts except Honor's display a post excerpt with each post listed on the blog's table of contents. If the first thing in a post is a heading or other special formatting, the excerpt may cause the table of contents to look not too pretty. This can be changed my removing the '{{ post.excerpt }}' line from the corresponding layout file or by simply adding a line of regular text before your heading.
