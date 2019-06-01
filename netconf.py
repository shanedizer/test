import json, getopt, sys
fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]
unixOptions = "hf:"
gnuOptions = ["help", "file="]
try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    sys.exit(2)
for currentArgument, currentValue in arguments:
    if currentArgument in ("-h", "--help"):
        print ("!!!HELP!!! Sorry, they didn't hear me...")
        sys.exit(0)
    elif currentArgument in ("-f", "--file"):
      json_conf=currentValue
NET_CONF_PATH="/etc/network/interfaces"
MTU=8986
networks = json.load(open(json_conf))
for interface, iface in networks.iteritems():
  for configs in iface:
    conf_file_path=NET_CONF_PATH
    conf_file = open(conf_file_path, "a")
    conf_file.write("auto {}.{}\n".format(interface, configs["vlan"]))
    conf_file.write("   iface {}.{} inet static\n".format(interface, configs["vlan"]))
    conf_file.write("   address {}\n".format(configs["ipaddr"]))
    conf_file.write("   netmask {}\n".format(configs["netmask"]))
    if "gateway" in configs:
      conf_file.write("   gateway {}\n".format(configs["gateway"]))
    if "dns-nameservers" in configs:
      conf_file.write("   dns-nameservers {}\n".format(configs["dns-nameservers"]))
    if "domain" in configs:
      conf_file.write("   dns-search {}\n".format(configs["domain"]))
    conf_file.write("   mtu {}\n".format(MTU))
    conf_file.close
