import { useState } from "react";

export function RegisterUser() {
    const [user, setUser] = useState({
        username: "",
        email: "",
        password: "",
        password2: "",
    });

    const { username, email, password, password2 } = user;

    const onChange = (e) => {
        setUser({ ...user, [e.target.name]: e.target.value });
    };

    const onSubmit = (e) => {
        e.preventDefault();
        console.log("Register Submit");
    };

    return (
        <div>
            <h2>Register</h2>
            <form onSubmit={onSubmit}>
                <div>
                    <label htmlFor="username">Username</label>
                    <input
                        type="text"
                        name="username"
                        value={username}
                        onChange={onChange}
                    />
                </div>
                <div>
                    <label htmlFor="email">Email</label>
                    <input
                        type="email"
                        name="email"
                        value={email}
                        onChange={onChange}
                    />
                </div>
                <div>
                    <label htmlFor="password">Password</label>
                    <input
                        type="password"
                        name="password"
                        value={password}
                        onChange={onChange}
                    />
                </div>
                <div>
                    <label htmlFor="password2">Confirm Password</label>
                    <input
                        type="password"
                        name="password2"
                        value={password2}
                        onChange={onChange}
                    />
                </div>
                <input type="submit" value="Register" />
            </form>
        </div>
    )
}