<div align="center">

# How to Use
</div>

Each item or folder in the root directory of this repository (apart from this **README.md**) is a functional module for **rasbot**.

To get it working, all you need to do is drop it into the `modules` folder of your **rasbot**, and then import it with a command.
> e.g., move `localtime.py` to `modules/` and run `r!cmdadd time &localtime&`.

For modules in folders, pass the full directory to the module.
> e.g., for the osu! Requests module, you need to run `r!cmdadd request &osu/request&` instead.

*These modules are not likely to be maintained as much as other modules, and are often one-offs done by request for streamers who use **rasbot**.*

<div align="center">

# What is "rasbot"?
</div>

**rasbot** is a Python-based Twitch bot that lets you see and modify **everything** going on behind the scenes.<br/>

rasbot is designed modularly and allows you to add to the base application easily with *"plug-and-play"*-style extensions. You can see some sample modules, **including** built-in functions in the `modules` folder.

To include a module as part of a command, encompass the module name in `&`, e.g.:
```
r!cmdadd np &np&
```

*For documentation on configuring modules or creating your own, see [this](https://github.com/jack-avery/rasbot/blob/master/modules/README.md).*