---
title: JAX-RS 入门
date: 2024-05-28 13:15:24
categories:
- [编程语言, Java]
tags:
- Java
- Jakarta EE
---

JAX-RS 是 Jakarta RESTful Web Services 的缩写，是 Jakarta EE API 规范，用于构建 RESTful 风格的 Web 服务。

本文通过一个简单的内存版的用户管理系统，介绍 JAX-RS 的基本用法。

<!-- more -->

## 使用 Quarkus REST 创建 JAX-RS 服务

为了便于演示，我们使用 Quarkus REST 来创建 JAX-RS 服务。

{% asset_img quarkus-create.png %}

## JAX-RS 常用注解

- `@Path`：指定资源类或方法的路径。
- `@GET`：指定方法可以通过 GET 方法访问。
- `@POST`：指定方法可以通过 POST 方法访问。
- `@PUT`：指定方法可以通过 PUT 方法访问。
- `@DELETE`：指定方法可以通过 DELETE 方法访问。
- `@PATCH`：指定方法可以通过 PATCH 方法访问。
- `@Consumes`：指定方法可以接受的 MIME 类型。
- `@Produces`：指定方法可以生成的 MIME 类型。

## 用户实体类

```java
public class User {
    private Integer id;
    private String name;
    private Integer age;

    // constructor, getter and setter...
}
```

## DAO 类

```java
public interface UserDao {
    User addUser(User user);
    boolean updateUser(Integer id, User user);
    boolean deleteUser(Integer id);
    User getUser(Integer id);
    List<User> getUsers();
}
```

此处我们使用一个 `List` 来模拟数据库。

```java
@Singleton
public class UserDaoImpl implements UserDao {
    private final List<User> users = new CopyOnWriteArrayList<>();

    @Override
    public User addUser(User user) {
        if (users.stream().anyMatch(u -> u.getId().equals(user.getId()))) {
            return null;
        }
        users.add(user);
        return user;
    }

    @Override
    public boolean updateUser(Integer id, User user) {
        for (var i = 0; i < users.size(); i++) {
            if (users.get(i).getId().equals(id)) {
                users.set(i, user);
                return true;
            }
        }
        return false;
    }

    @Override
    public boolean deleteUser(Integer id) {
        return users.removeIf(u -> u.getId().equals(id));
    }

    @Override
    public User getUser(Integer id) {
        return users.stream().filter(u -> u.getId().equals(id)).findFirst().orElse(null);
    }

    @Override
    public List<User> getUsers() {
        return new ArrayList<>(users);
    }
}
```

## `UserResource` 类

```java
@Path("/user")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class UserResource {
    private final UserDao userDao;

    public UserResource(UserDao userDao) {
        this.userDao = userDao;
    }

    @GET
    public Response getUsers() {
        return Response.ok(userDao.getUsers()).build();
    }

    @GET
    @Path("/{id}")
    public Response getUser(@PathParam("id") Integer id) {
        User user = userDao.getUser(id);
        if (user == null) {
            return Response.status(Response.Status.NOT_FOUND).build();
        }
        return Response.ok(user).build();
    }

    @POST
    public Response addUser(User user) {
        User u = userDao.addUser(user);
        if (u == null) {
            return Response.status(Response.Status.CONFLICT).build();
        }
        return Response.ok(u).build();
    }

    @PUT
    @Path("/{id}")
    public Response updateUser(@PathParam("id") Integer id, User user) {
        if (!userDao.updateUser(id, user)) {
            return Response.status(Response.Status.NOT_FOUND).build();
        }
        return Response.ok().build();
    }

    @DELETE
    @Path("/{id}")
    public Response deleteUser(@PathParam("id") Integer id) {
        if (!userDao.deleteUser(id)) {
            return Response.status(Response.Status.NOT_FOUND).build();
        }
        return Response.ok().build();
    }
}
```

代码仓库：<https://github.com/gtn1024/jaxrs-demo>
