# Demo

Here's an example LUA-language NSE script to be executed in Nmap.

```lua
-- HEAD --

description = [[
This is a simple script example that determines if a port is open.
]]

author = "Ned Flanders"

-- RULE --

portrule = function(host, port)
 return port.protocol == "tcp"
 and port.state == "open"
end

-- ACTION --

action = function(host, port)
 return "This port is open!"
end
```
