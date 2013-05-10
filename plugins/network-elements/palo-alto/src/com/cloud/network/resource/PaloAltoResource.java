// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the 
// specific language governing permissions and limitations
// under the License.
package com.cloud.network.resource;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.StringReader;
import java.net.Socket;
import java.net.SocketTimeoutException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.apache.commons.codec.binary.Base64;
import java.nio.ByteBuffer;
import java.util.UUID;

import javax.naming.ConfigurationException;
import javax.xml.parsers.DocumentBuilderFactory;

import org.apache.log4j.Logger;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

import com.cloud.agent.IAgentControl;
import com.cloud.agent.api.Answer;
import com.cloud.agent.api.Command;
import com.cloud.agent.api.ExternalNetworkResourceUsageAnswer;
import com.cloud.agent.api.ExternalNetworkResourceUsageCommand;
import com.cloud.agent.api.MaintainAnswer;
import com.cloud.agent.api.MaintainCommand;
import com.cloud.agent.api.PingCommand;
import com.cloud.agent.api.ReadyAnswer;
import com.cloud.agent.api.ReadyCommand;
import com.cloud.agent.api.StartupCommand;
import com.cloud.agent.api.StartupExternalFirewallCommand;
import com.cloud.agent.api.routing.IpAssocAnswer;
import com.cloud.agent.api.routing.IpAssocCommand;
import com.cloud.agent.api.routing.NetworkElementCommand;
import com.cloud.agent.api.routing.SetFirewallRulesCommand;
import com.cloud.agent.api.routing.SetPortForwardingRulesCommand;
import com.cloud.agent.api.routing.SetStaticNatRulesCommand;
import com.cloud.agent.api.to.FirewallRuleTO;
import com.cloud.agent.api.to.IpAddressTO;
import com.cloud.agent.api.to.PortForwardingRuleTO;
import com.cloud.agent.api.to.StaticNatRuleTO;
import com.cloud.host.Host;
import com.cloud.network.rules.FirewallRule;
import com.cloud.network.rules.FirewallRule.Purpose;
import com.cloud.resource.ServerResource;
import com.cloud.utils.NumbersUtil;
import com.cloud.utils.exception.ExecutionException;
import com.cloud.utils.net.NetUtils;
import com.cloud.utils.script.Script;

import org.apache.http.client.ResponseHandler;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.NameValuePair;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.protocol.HTTP;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.net.URLDecoder;
import javax.xml.xpath.XPathFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpressionException;
import com.cloud.network.utils.HttpClientWrapper;


import javax.xml.transform.stream.StreamSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Source;
import java.io.StringWriter;

public class PaloAltoResource implements ServerResource {

    private String _name;
    private String _zoneId;
    private String _ip;
    private String _username;
    private String _password;
    private String _guid;
    private String _key;
    private String _objectNameWordSep;
    private Integer _numRetries;
    private Integer _timeoutInSeconds;
    private String _publicZone;
    private String _privateZone;
    private String _publicInterface;
    private String _privateInterface;
    private String _publicInterfaceType;
    private String _privateInterfaceType;
    private String _virtualRouter;
    private String _usageInterface;
    private String _pingManagementProfile;
//    private UsageFilter _usageFilterVlanInput;
//    private UsageFilter _usageFilterVlanOutput;
//    private UsageFilter _usageFilterIPInput;
//    private UsageFilter _usageFilterIPOutput;
    private final Logger s_logger = Logger.getLogger(PaloAltoResource.class);

    private static String _apiUri = "/api";
    private static HttpClient _httpclient;

    private enum PaloAltoMethod {
        GET,
        POST;
    }

    private enum PaloAltoXml {
        SECURITY_POLICY_ADD("security-policy-add.xml"),
        SOURCE_NAT_ADD("source-nat-add.xml");

        private String scriptsDir = "scripts/network/palo_alto";
        private String xml;
        private final Logger s_logger = Logger.getLogger(PaloAltoResource.class);

        private PaloAltoXml(String filename) {
            this.xml = getXml(filename);
        }

        public String getXml() {
            return xml;
        }

        private String getXml(String filename) {
            try {
                String xmlFilePath = Script.findScript(scriptsDir, filename);

                if (xmlFilePath == null) {
                    throw new Exception("Failed to find Palo Alto XML file: " + filename);
                }

                FileReader fr = new FileReader(xmlFilePath);
                BufferedReader br = new BufferedReader(fr);

                String xml = "";
                String line;
                while ((line = br.readLine()) != null) {
                    xml += line.trim();
                }

                return xml;
            } catch (Exception e) {
                s_logger.debug(e);
                return null;
            }
        }
    }   

//    public class UsageFilter {
//        private String name;
//        private String counterIdentifier;
//        private String addressType;
//
//        private UsageFilter(String name, String addressType, String counterIdentifier) {
//            this.name = name;           
//            this.addressType = addressType;
//
//            if (_usageInterface != null) {
//                counterIdentifier = _usageInterface + counterIdentifier;
//            }
//
//            this.counterIdentifier = counterIdentifier;
//        }
//
//        public String getName() {
//            return name;
//        }
//
//        public String getCounterIdentifier() {
//            return counterIdentifier;
//        }
//
//        public String getAddressType() {
//            return addressType;
//        }
//    }   


    private enum InterfaceType {
        AGGREGATE("aggregate-ethernet"),
        ETHERNET("ethernet");

        private String type;

        private InterfaceType(String type) {
            this.type = type;
        }
        public String toString() {
            return type;
        }
    }

    private enum PaloAltoPrimative {
        CHECK_IF_EXISTS, ADD, DELETE;
    }

    private enum Protocol {
        tcp, udp, icmp, any;
    }

//    private enum RuleMatchCondition {
//        ALL,
//        PUBLIC_PRIVATE_IPS,
//        PRIVATE_SUBNET;
//    }

    private enum GuestNetworkType {
        SOURCE_NAT,
        INTERFACE_NAT;
    }

//    private enum SecurityPolicyType {
//        STATIC_NAT("staticnat"),
//        DESTINATION_NAT("destnat"),
//        VPN("vpn");
//
//        private String identifier;
//
//        private SecurityPolicyType(String identifier) {
//            this.identifier = identifier;
//        }
//
//        private String getIdentifier() {
//            return identifier;
//        }
//    }

    public Answer executeRequest(Command cmd) {
        if (cmd instanceof ReadyCommand) {
            return execute((ReadyCommand) cmd);
        } else if (cmd instanceof MaintainCommand) {
            return execute((MaintainCommand) cmd);
        } else if (cmd instanceof IpAssocCommand) {
            return execute((IpAssocCommand) cmd);
        } else if (cmd instanceof SetStaticNatRulesCommand) {
            return execute((SetStaticNatRulesCommand) cmd);
        } else if (cmd instanceof SetPortForwardingRulesCommand) {
            return execute((SetPortForwardingRulesCommand) cmd);
        } else if (cmd instanceof SetFirewallRulesCommand) {
            return execute((SetFirewallRulesCommand) cmd);
        } else if (cmd instanceof ExternalNetworkResourceUsageCommand) {
            return execute((ExternalNetworkResourceUsageCommand) cmd);
        } else {
            return Answer.createUnsupportedCommandAnswer(cmd);
        }
    }

    public boolean configure(String name, Map<String, Object> params) throws ConfigurationException {
        try {
            _name = (String) params.get("name");
            if (_name == null) {
                throw new ConfigurationException("Unable to find name");
            }

            _zoneId = (String) params.get("zoneId");
            if (_zoneId == null) {
                throw new ConfigurationException("Unable to find zone");
            }

            _ip = (String) params.get("ip");
            if (_ip == null) {
                throw new ConfigurationException("Unable to find IP");
            }

            _username = (String) params.get("username");
            if (_username == null) {
                throw new ConfigurationException("Unable to find username");
            }

            _password = (String) params.get("password");
            if (_password == null) {
                throw new ConfigurationException("Unable to find password");
            }           

            _publicInterface = (String) params.get("publicinterface");
            if (_publicInterface == null) {
                throw new ConfigurationException("Unable to find public interface.");
            }

            _privateInterface = (String) params.get("privateinterface");
            if (_privateInterface == null) {
                throw new ConfigurationException("Unable to find private interface.");
            }

            _publicZone = (String) params.get("publicnetwork");
            if (_publicZone == null) {
                throw new ConfigurationException("Unable to find public zone");
            }

            _privateZone = (String) params.get("privatenetwork");
            if (_privateZone == null) {
                throw new ConfigurationException("Unable to find private zone");
            }

            _virtualRouter = (String) params.get("externalvirtualrouter");
            if (_virtualRouter == null) {
                throw new ConfigurationException("Unable to find virtual router");
            }

            _guid = (String)params.get("guid");
            if (_guid == null) {
                throw new ConfigurationException("Unable to find the guid");
            }

            _numRetries = NumbersUtil.parseInt((String) params.get("numretries"), 1);

            _timeoutInSeconds = NumbersUtil.parseInt((String) params.get("timeout"), 300);

            _objectNameWordSep = "-";
            
//            _ikeProposalName = "cloud-ike-proposal";
//            _ipsecPolicyName = "cloud-ipsec-policy";
//            _ikeGatewayHostname = "cloud";
//            _vpnObjectPrefix = "vpn-a";
//            _primaryDnsAddress = "4.2.2.2";

            // Open a socket and login
            if (!refreshPaloAltoConnection()) {
                throw new ConfigurationException("Unable to open a connection to the Palo Alto.");
            }

            try {
                _publicInterfaceType = getInterfaceType(_publicInterface);
                if (_publicInterfaceType.equals("")) {
                    throw new ConfigurationException("The configured public interface is not configured on the Palo Alto.");
                }
            } catch (ExecutionException e) {
                throw new ConfigurationException(e.getMessage());
            }

            try {
                _privateInterfaceType = getInterfaceType(_privateInterface);
                if (_privateInterfaceType.equals("")) {
                    throw new ConfigurationException("The configured private interface is not configured on the Palo Alto.");
                }
            } catch (ExecutionException e) {
                throw new ConfigurationException(e.getMessage());
            }

            _pingManagementProfile = "Ping";
            try {
                ArrayList<IPaloAltoCommand> cmdList = new ArrayList<IPaloAltoCommand>();
                managePingProfile(cmdList, PaloAltoPrimative.ADD);
                boolean status = requestWithCommit(cmdList);
            } catch (ExecutionException e) {
                throw new ConfigurationException(e.getMessage());
            }
            

//            _publicZoneInputFilterName = _publicZone;
            
//            _usageFilterVlanInput = new UsageFilter("vlan-input", null, "vlan-input");
//            _usageFilterVlanOutput = new UsageFilter("vlan-output", null, "vlan-output");
//            _usageFilterIPInput = new UsageFilter(_publicZone, "destination-address", "-i");
//            _usageFilterIPOutput = new UsageFilter(_privateZone, "source-address", "-o");

            return true;
        } catch (Exception e) {
            throw new ConfigurationException(e.getMessage());
        }

    }

    public StartupCommand[] initialize() {   
        StartupExternalFirewallCommand cmd = new StartupExternalFirewallCommand();
        cmd.setName(_name);
        cmd.setDataCenter(_zoneId);
        cmd.setPod("");
        cmd.setPrivateIpAddress(_ip);
        cmd.setStorageIpAddress("");
        cmd.setVersion(PaloAltoResource.class.getPackage().getImplementationVersion());
        cmd.setGuid(_guid);
        return new StartupCommand[]{cmd};
    }

    public Host.Type getType() {
        return Host.Type.ExternalFirewall;
    }

    @Override
    public String getName() {
        return _name;
    }

    @Override
    public boolean start() {
        return true;
    }

    @Override
    public boolean stop() {
        return true;
    }

    @Override
    public PingCommand getCurrentStatus(final long id) {
        return new PingCommand(Host.Type.ExternalFirewall, id);
    }

    @Override
    public void disconnected() {
        // nothing for now...
    }

    public IAgentControl getAgentControl() {
        return null;
    }

    public void setAgentControl(IAgentControl agentControl) {
        return;
    }

    private Answer execute(ReadyCommand cmd) {
        return new ReadyAnswer(cmd);
    }

    private Answer execute(MaintainCommand cmd) {
        return new MaintainAnswer(cmd);
    }

    private ExternalNetworkResourceUsageAnswer execute(ExternalNetworkResourceUsageCommand cmd) {
        try {   
            return getUsageAnswer(cmd);
        } catch (ExecutionException e) {
            return new ExternalNetworkResourceUsageAnswer(cmd, e);
        }
    }

    /*
     * Login
     */
    private void openHttpConnection(){
        _httpclient = new DefaultHttpClient();

        // Allows you to connect via SSL using unverified certs
        _httpclient = HttpClientWrapper.wrapClient(_httpclient);
    }

    private boolean refreshPaloAltoConnection() {
        if (_httpclient == null) {
            openHttpConnection();
        }

        try {
            return login(_username, _password);
        } catch (ExecutionException e) {
            s_logger.error("Failed to login due to " + e.getMessage());
            return false;
        }
    }

    private boolean login(String username, String password) throws ExecutionException {
        Map<String, String> params = new HashMap<String, String>();
        params.put("type", "keygen");
        params.put("user", username);
        params.put("password", password);

        String keygenBody;
        try {
            keygenBody = request(PaloAltoMethod.GET, params);    
        } catch (ExecutionException e) {
            return false;
        }
        Document keygen_doc = getDocument(keygenBody);
        XPath xpath = XPathFactory.newInstance().newXPath();
        try {
            XPathExpression expr = xpath.compile("/response[@status='success']/result/key/text()");
            _key = (String) expr.evaluate(keygen_doc, XPathConstants.STRING);
        } catch (XPathExpressionException e) {
            throw new ExecutionException(e.getCause().getMessage());
        }
        if (_key != null) {
            return true;
        }
        return false;
    }


    /*
     * Guest networks
     */

    private synchronized Answer execute(IpAssocCommand cmd) {
        refreshPaloAltoConnection();
        return execute(cmd, _numRetries);
    }

    private Answer execute(IpAssocCommand cmd, int numRetries) {        
        String[] results = new String[cmd.getIpAddresses().length];
        int i = 0;
        try {
            IpAddressTO ip;
            if (cmd.getIpAddresses().length != 1) {
                throw new ExecutionException("Received an invalid number of guest IPs to associate.");
            } else {
                ip = cmd.getIpAddresses()[0];
            }                               

            String sourceNatIpAddress = null; 
            GuestNetworkType type = GuestNetworkType.INTERFACE_NAT;

            if (ip.isSourceNat()) {
                type = GuestNetworkType.SOURCE_NAT;

                if (ip.getPublicIp() == null) {
                    throw new ExecutionException("Source NAT IP address must not be null.");
                } else {
                    sourceNatIpAddress = ip.getPublicIp();
                }
            }

            long guestVlanTag = Long.parseLong(cmd.getAccessDetail(NetworkElementCommand.GUEST_VLAN_TAG));
            String guestVlanGateway = cmd.getAccessDetail(NetworkElementCommand.GUEST_NETWORK_GATEWAY);
            String cidr = cmd.getAccessDetail(NetworkElementCommand.GUEST_NETWORK_CIDR);
            long cidrSize = NetUtils.cidrToLong(cidr)[1];
            String guestVlanSubnet = NetUtils.getCidrSubNet(guestVlanGateway, cidrSize);    
            
            Long publicVlanTag = null;
            if (ip.getVlanId() != null && !ip.getVlanId().equals("untagged")) {
                try {
                    publicVlanTag = Long.parseLong(ip.getVlanId());
                } catch (Exception e) {
                    throw new ExecutionException("Could not parse public VLAN tag: " + ip.getVlanId());
                }
            } 

            ArrayList<IPaloAltoCommand> commandList = new ArrayList<IPaloAltoCommand>();

            // Remove the guest network:
            // Remove source, static, and destination NAT rules
            // Remove VPN 
            shutdownGuestNetwork(commandList, type, publicVlanTag, sourceNatIpAddress, guestVlanTag, guestVlanGateway, guestVlanSubnet, cidrSize);
            s_logger.debug("Shutdown Command List: "+commandList.size());

            if (ip.isAdd()) {                                 
                // Implement the guest network for this VLAN
                implementGuestNetwork(commandList, type, publicVlanTag, sourceNatIpAddress, guestVlanTag, guestVlanGateway, guestVlanSubnet, cidrSize);
                s_logger.debug("Implement Command List: "+commandList.size());
                
            }

            boolean status = requestWithCommit(commandList);

            results[i++] = ip.getPublicIp() + " - success";
        } catch (ExecutionException e) {
            s_logger.error(e);

            if (numRetries > 0 && refreshPaloAltoConnection()) {
                int numRetriesRemaining = numRetries - 1;
                s_logger.debug("Retrying IPAssocCommand. Number of retries remaining: " + numRetriesRemaining);
                return execute(cmd, numRetriesRemaining);
            } else {
                results[i++] = IpAssocAnswer.errorResult;
            }
        }

        return new IpAssocAnswer(cmd, results);
    }

    private void implementGuestNetwork(ArrayList<IPaloAltoCommand> cmdList, GuestNetworkType type, Long publicVlanTag, String publicIp, long privateVlanTag, String privateGateway, String privateSubnet, long privateCidrNumber) throws ExecutionException {
        privateGateway = privateGateway + "/" + privateCidrNumber;
        privateSubnet = privateSubnet + "/" + privateCidrNumber;

        if (publicIp != null) {
            publicIp = publicIp+"/32";
        }

        managePrivateInterface(cmdList, PaloAltoPrimative.ADD, privateVlanTag, privateGateway);

        if (type.equals(GuestNetworkType.SOURCE_NAT)) {
            managePublicInterface(cmdList, PaloAltoPrimative.ADD, publicVlanTag, publicIp, privateVlanTag);
            manageSrcNatRule(cmdList, PaloAltoPrimative.ADD, type, publicVlanTag, publicIp, privateVlanTag, privateGateway);         
            //--manageUsageFilter(PaloAltoPrimative.ADD, _usageFilterIPOutput, privateSubnet, null, genIpFilterTermName(publicIp));
            //--manageUsageFilter(PaloAltoPrimative.ADD, _usageFilterIPInput, publicIp, null, genIpFilterTermName(publicIp));
        } else if (type.equals(GuestNetworkType.INTERFACE_NAT)){            
            //--manageUsageFilter(PaloAltoPrimative.ADD, _usageFilterVlanOutput, null, privateVlanTag, null);          
            //--manageUsageFilter(PaloAltoPrimative.ADD, _usageFilterVlanInput, null, privateVlanTag, null);
        }

        String msg = "Implemented guest network with type " + type + ". Guest VLAN tag: " + privateVlanTag + ", guest gateway: " + privateGateway;
        msg += type.equals(GuestNetworkType.SOURCE_NAT) ? ", source NAT IP: " + publicIp : "";
        s_logger.debug(msg);
    }

    private void shutdownGuestNetwork(ArrayList<IPaloAltoCommand> cmdList, GuestNetworkType type, Long publicVlanTag, String sourceNatIpAddress, long privateVlanTag, String privateGateway, String privateSubnet, long privateCidrSize) throws ExecutionException {     
        // Remove static and destination NAT rules for the guest network
        //removeStaticAndDestNatRulesInPrivateVlan(privateVlanTag, privateGateway, privateCidrSize);

        privateGateway = privateGateway + "/" + privateCidrSize;
        privateSubnet = privateSubnet + "/" + privateCidrSize;

        if (sourceNatIpAddress != null) {
            sourceNatIpAddress = sourceNatIpAddress+"/32";
        }

        if (type.equals(GuestNetworkType.SOURCE_NAT)) {
            manageSrcNatRule(cmdList, PaloAltoPrimative.DELETE, type, publicVlanTag, sourceNatIpAddress, privateVlanTag, privateGateway);
            managePublicInterface(cmdList, PaloAltoPrimative.DELETE, publicVlanTag, sourceNatIpAddress, privateVlanTag);  
            //--manageUsageFilter(PaloAltoPrimative.DELETE, _usageFilterIPOutput, privateSubnet, null, genIpFilterTermName(sourceNatIpAddress));
            //--manageUsageFilter(PaloAltoPrimative.DELETE, _usageFilterIPInput, sourceNatIpAddress, null, genIpFilterTermName(sourceNatIpAddress));                                                                  
        } else if (type.equals(GuestNetworkType.INTERFACE_NAT)) {
            //--manageUsageFilter(PaloAltoPrimative.DELETE, _usageFilterVlanOutput, null, privateVlanTag, null);         
            //--manageUsageFilter(PaloAltoPrimative.DELETE, _usageFilterVlanInput, null, privateVlanTag, null);                        
        }      

        managePrivateInterface(cmdList, PaloAltoPrimative.DELETE, privateVlanTag, privateGateway);       

        String msg = "Shut down guest network with type " + type +". Guest VLAN tag: " + privateVlanTag + ", guest gateway: " + privateGateway;
        msg += type.equals(GuestNetworkType.SOURCE_NAT) ? ", source NAT IP: " + sourceNatIpAddress : "";
        s_logger.debug(msg);
    }

    



    /* Firewall rules */
    private synchronized Answer execute(SetFirewallRulesCommand cmd) {
        refreshPaloAltoConnection();
        return execute(cmd, _numRetries);
    }
    
    private Answer execute(SetFirewallRulesCommand cmd, int numRetries) {
        FirewallRuleTO[] rules = cmd.getRules();
        try {
            //openConfiguration();
            boolean thr = false;
            if (thr) {
                throw(new ExecutionException("fake error"));
            }

            for (FirewallRuleTO rule : rules) {
                int startPort = 0, endPort = 0;
                if (rule.getSrcPortRange() != null) {
                    startPort = rule.getSrcPortRange()[0];
                    endPort = rule.getSrcPortRange()[1];
                }
                //FirewallFilterTerm term = new FirewallFilterTerm(genIpIdentifier(rule.getSrcIp()) + "-" + String.valueOf(rule.getId()), rule.getSourceCidrList(), 
                //        rule.getSrcIp(), rule.getProtocol(), startPort, endPort,
                //        rule.getIcmpType(), rule.getIcmpCode(), genIpIdentifier(rule.getSrcIp()) + _usageFilterIPInput.getCounterIdentifier());
                //if (!rule.revoked()) {
                //    //manageFirewallFilter(PaloAltoPrimative.ADD, term, _publicZoneInputFilterName);
                //} else {
                //    //manageFirewallFilter(PaloAltoPrimative.DELETE, term, _publicZoneInputFilterName);
                //}
            }
                
            //commitConfiguration();
            return new Answer(cmd);
        } catch (ExecutionException e) {
            s_logger.error(e);
            //closeConfiguration();

            if (numRetries > 0 && refreshPaloAltoConnection()) {
                int numRetriesRemaining = numRetries - 1;
                s_logger.debug("Retrying SetFirewallRulesCommand. Number of retries remaining: " + numRetriesRemaining);
                return execute(cmd, numRetriesRemaining);
            } else {
                return new Answer(cmd, e);
            }
        }
    }

    /*
     * Static NAT
     */

    private synchronized Answer execute(SetStaticNatRulesCommand cmd) {
        refreshPaloAltoConnection();
        return execute(cmd, _numRetries);
    }       

    private Answer execute(SetStaticNatRulesCommand cmd, int numRetries) {      
        StaticNatRuleTO[] allRules = cmd.getRules();
        //Map<String, ArrayList<FirewallRuleTO>> activeRules = getActiveRules(allRules);
        //Map<String, String> vlanTagMap = getVlanTagMap(allRules);

        try {
            boolean thr = false;
            if (thr) {
                throw(new ExecutionException("fake error"));
            }
//            //openConfiguration();
//
//            Set<String> ipPairs = activeRules.keySet();
//            for (String ipPair : ipPairs) {             
//                String[] ipPairComponents = ipPair.split("-");
//                String publicIp = ipPairComponents[0];
//                String privateIp = ipPairComponents[1];                                                                     
//
//                List<FirewallRuleTO> activeRulesForIpPair = activeRules.get(ipPair);      
//                //Long publicVlanTag = getVlanTag(vlanTagMap.get(publicIp));
//
//                // Delete the existing static NAT rule for this IP pair
//                //removeStaticNatRule(publicVlanTag, publicIp, privateIp);
//
//                if (activeRulesForIpPair.size() > 0) {
//                    // If there are active FirewallRules for this IP pair, add the static NAT rule and open the specified port ranges
//                    //addStaticNatRule(publicVlanTag, publicIp, privateIp, activeRulesForIpPair);
//                } 
//            }           

            //commitConfiguration();
            return new Answer(cmd);
        } catch (ExecutionException e) {
            s_logger.error(e);
            //closeConfiguration();

            if (numRetries > 0 && refreshPaloAltoConnection()) {
                int numRetriesRemaining = numRetries - 1;
                s_logger.debug("Retrying SetPortForwardingRulesCommand. Number of retries remaining: " + numRetriesRemaining);
                return execute(cmd, numRetriesRemaining);
            } else {
                return new Answer(cmd, e);
            }
        }
    }

//    private void addStaticNatRule(Long publicVlanTag, String publicIp, String privateIp, List<FirewallRuleTO> rules) throws ExecutionException {
//        //manageProxyArp(PaloAltoPrimative.ADD, publicVlanTag, publicIp);
//        //manageStaticNatRule(PaloAltoPrimative.ADD, publicIp, privateIp);
//        //manageAddressBookEntry(PaloAltoPrimative.ADD, _privateZone, privateIp, null);
//
//        // Add a new security policy with the current set of applications
//        //addSecurityPolicyAndApplications(SecurityPolicyType.STATIC_NAT, privateIp, extractApplications(rules));
//
//        s_logger.debug("Added static NAT rule for public IP " + publicIp + ", and private IP " + privateIp);
//    }       

//    private void removeStaticNatRule(Long publicVlanTag, String publicIp, String privateIp) throws ExecutionException {     
//        //manageStaticNatRule(PaloAltoPrimative.DELETE, publicIp, privateIp);
//        //manageProxyArp(PaloAltoPrimative.DELETE, publicVlanTag, publicIp);   
//
//        // Remove any existing security policy and clean up applications
//        //removeSecurityPolicyAndApplications(SecurityPolicyType.STATIC_NAT, privateIp);
//
//        //manageAddressBookEntry(PaloAltoPrimative.DELETE, _privateZone, privateIp, null);     
//
//        s_logger.debug("Removed static NAT rule for public IP " + publicIp + ", and private IP " + privateIp);
//    }

//    private void removeStaticNatRules(Long privateVlanTag, Map<String, Long> publicVlanTags, List<String[]> staticNatRules) throws ExecutionException {
//        for (String[] staticNatRuleToRemove : staticNatRules) {
//            String staticNatRulePublicIp = staticNatRuleToRemove[0];
//            String staticNatRulePrivateIp = staticNatRuleToRemove[1];
//            
//            Long publicVlanTag = null;
//            if (publicVlanTags.containsKey(staticNatRulePublicIp)) {
//                publicVlanTag = publicVlanTags.get(staticNatRulePublicIp);
//            }
//
//            if (privateVlanTag != null) {
//                s_logger.warn("Found a static NAT rule (" + staticNatRulePublicIp + " <-> " + staticNatRulePrivateIp + ") for guest VLAN with tag " + privateVlanTag + " that is active when the guest network is being removed. Removing rule...");
//            }
//
//            //removeStaticNatRule(publicVlanTag, staticNatRulePublicIp, staticNatRulePrivateIp);
//        }
//    }
    

    /*
     * Destination NAT
     */

    private synchronized Answer execute (SetPortForwardingRulesCommand cmd) {
        refreshPaloAltoConnection();
        return execute(cmd, _numRetries);
    }

    private Answer execute(SetPortForwardingRulesCommand cmd, int numRetries) {     
        PortForwardingRuleTO[] allRules = cmd.getRules();
        //Map<String, ArrayList<FirewallRuleTO>> activeRules = getActiveRules(allRules);

        try {
            boolean thr = false;
            if (thr) {
                throw(new ExecutionException("fake error"));
            }
            //openConfiguration();

//            Set<String> ipPairs = activeRules.keySet();
//            for (String ipPair : ipPairs) {             
//                String[] ipPairComponents = ipPair.split("-");
//                String publicIp = ipPairComponents[0];
//                String privateIp = ipPairComponents[1];                                                                     
//
//                List<FirewallRuleTO> activeRulesForIpPair = activeRules.get(ipPair);                
//
//                // Get a list of all destination NAT rules for the public/private IP address pair
//                //List<String[]> destNatRules = getDestNatRules(RuleMatchCondition.PUBLIC_PRIVATE_IPS, publicIp, privateIp, null, null);
//                //Map<String, Long> publicVlanTags = getPublicVlanTagsForNatRules(destNatRules);
//
//                // Delete all of these rules, along with the destination NAT pools and security policies they use
//                //removeDestinationNatRules(null, publicVlanTags, destNatRules);
//
//                // If there are active rules for the public/private IP address pair, add them back
//                for (FirewallRuleTO rule : activeRulesForIpPair) {
//                    //Long publicVlanTag = getVlanTag(rule.getSrcVlanTag());
//                    PortForwardingRuleTO portForwardingRule = (PortForwardingRuleTO) rule;
//                    //addDestinationNatRule(getProtocol(rule.getProtocol()), publicVlanTag, portForwardingRule.getSrcIp(), portForwardingRule.getDstIp(), 
//                    //                      portForwardingRule.getSrcPortRange()[0], portForwardingRule.getSrcPortRange()[1],
//                    //                      portForwardingRule.getDstPortRange()[0], portForwardingRule.getDstPortRange()[1]);
//                }
//            }           

            //commitConfiguration();
            return new Answer(cmd);
        } catch (ExecutionException e) {
            s_logger.error(e);
            //closeConfiguration();

            if (numRetries > 0 && refreshPaloAltoConnection()) {
                int numRetriesRemaining = numRetries - 1;
                s_logger.debug("Retrying SetPortForwardingRulesCommand. Number of retries remaining: " + numRetriesRemaining);
                return execute(cmd, numRetriesRemaining);
            } else {
                return new Answer(cmd, e);
            }
        }
    }

//    private void addDestinationNatRule(Protocol protocol, Long publicVlanTag, String publicIp, String privateIp, int srcPortStart, int srcPortEnd, int destPortStart, int destPortEnd) throws ExecutionException {
//        //manageProxyArp(PaloAltoPrimative.ADD, publicVlanTag, publicIp);       
//        
//        int offset = 0;
//        for (int srcPort = srcPortStart; srcPort <= srcPortEnd; srcPort++) {
//            int destPort = destPortStart + offset;
//            //manageDestinationNatPool(PaloAltoPrimative.ADD, privateIp, destPort);      
//            //manageDestinationNatRule(PaloAltoPrimative.ADD, publicIp, privateIp, srcPort, destPort); 
//            offset += 1;
//        }
//                
//        //manageAddressBookEntry(PaloAltoPrimative.ADD, _privateZone, privateIp, null);
//
//        List<Object[]> applications = new ArrayList<Object[]>();
//        applications.add(new Object[]{protocol, destPortStart, destPortEnd});
//        //addSecurityPolicyAndApplications(SecurityPolicyType.DESTINATION_NAT, privateIp, applications);
//
//        String srcPortRange = srcPortStart + "-" + srcPortEnd;
//        String destPortRange = destPortStart + "-" + destPortEnd;
//        s_logger.debug("Added destination NAT rule for protocol " + protocol + ", public IP " + publicIp + ", private IP " + privateIp +  ", source port range " + srcPortRange + ", and dest port range " + destPortRange);
//    }

//    private void removeDestinationNatRule(Long publicVlanTag, String publicIp, String privateIp, int srcPort, int destPort) throws ExecutionException {               
//        //manageDestinationNatRule(PaloAltoPrimative.DELETE, publicIp, privateIp, srcPort, destPort);
//        //manageDestinationNatPool(PaloAltoPrimative.DELETE, privateIp, destPort);   
//        //manageProxyArp(PaloAltoPrimative.DELETE, publicVlanTag, publicIp);    
//
//        //removeSecurityPolicyAndApplications(SecurityPolicyType.DESTINATION_NAT, privateIp);
//
//        //manageAddressBookEntry(PaloAltoPrimative.DELETE, _privateZone, privateIp, null);             
//
//        s_logger.debug("Removed destination NAT rule for public IP " + publicIp + ", private IP " + privateIp +  ", source port " + srcPort + ", and dest port " + destPort);   
//    }


//    private void removeDestinationNatRules(Long privateVlanTag, Map<String, Long> publicVlanTags, List<String[]> destNatRules) throws ExecutionException {
//        for (String[] destNatRule : destNatRules) {
//            String publicIp = destNatRule[0];
//            String privateIp = destNatRule[1];
//            int srcPort = Integer.valueOf(destNatRule[2]);
//            int destPort = Integer.valueOf(destNatRule[3]);
//            
//            Long publicVlanTag = null;
//            if (publicVlanTags.containsKey(publicIp)) {
//                publicVlanTag = publicVlanTags.get(publicIp);
//            }
//
//            if (privateVlanTag != null) {
//                s_logger.warn("Found a destination NAT rule (public IP: " + publicIp + ", private IP: " + privateIp + 
//                        ", public port: " + srcPort + ", private port: " + destPort + ") for guest VLAN with tag " + 
//                        privateVlanTag + " that is active when the guest network is being removed. Removing rule...");
//            }
//
//            removeDestinationNatRule(publicVlanTag, publicIp, privateIp, srcPort, destPort);
//        }
//    }
    
 

    /*
     * Private interfaces
     */

    private String genPrivateInterfaceName(long vlanTag) {
        return _privateInterface+"."+Long.toString(vlanTag);
    }

    public boolean managePrivateInterface(ArrayList<IPaloAltoCommand> cmdList, PaloAltoPrimative prim, long privateVlanTag, String privateGateway) throws ExecutionException {
        String _interfaceName =  genPrivateInterfaceName(privateVlanTag);

        switch (prim) {

        case CHECK_IF_EXISTS:
            // check if one exists already
            Map<String, String> params = new HashMap<String, String>();
            params.put("type", "config");
            params.put("action", "get");
            params.put("xpath", "/config/devices/entry/network/interface/"+_privateInterfaceType+"/entry[@name='"+_privateInterface+"']/layer3/units/entry[@name='"+_interfaceName+"']");
            String response = request(PaloAltoMethod.GET, params);
            boolean result = (validResponse(response) && responseNotEmpty(response));
            s_logger.debug("Private sub-interface exists: "+_interfaceName+", "+result);
            return result;

        case ADD:
            if (managePrivateInterface(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS, privateVlanTag, privateGateway)) {
                return true;
            }

            // add cmds
            // add sub-interface
            Map<String, String> a_sub_params = new HashMap<String, String>();
            a_sub_params.put("type", "config");
            a_sub_params.put("action", "set");
            a_sub_params.put("xpath", "/config/devices/entry/network/interface/"+_privateInterfaceType+"/entry[@name='"+_privateInterface+"']/layer3/units/entry[@name='"+_interfaceName+"']");
            a_sub_params.put("element", "<tag>"+privateVlanTag+"</tag><ip><entry name='"+privateGateway+"'/></ip><interface-management-profile>"+_pingManagementProfile+"</interface-management-profile>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_sub_params));

            // add sub-interface to VR...
            Map<String, String> a_vr_params = new HashMap<String, String>();
            a_vr_params.put("type", "config");
            a_vr_params.put("action", "set");
            a_vr_params.put("xpath", "/config/devices/entry/network/virtual-router/entry[@name='"+_virtualRouter+"']/interface");
            a_vr_params.put("element", "<member>"+_interfaceName+"</member>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_vr_params));

            // add sub-interface to vsys...
            Map<String, String> a_vsys_params = new HashMap<String, String>();
            a_vsys_params.put("type", "config");
            a_vsys_params.put("action", "set");
            a_vsys_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/import/network/interface");
            a_vsys_params.put("element", "<member>"+_interfaceName+"</member>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_vsys_params));

            // add sub-interface to zone...
            Map<String, String> a_zone_params = new HashMap<String, String>();
            a_zone_params.put("type", "config");
            a_zone_params.put("action", "set");
            a_zone_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/zone/entry[@name='"+_privateZone+"']/network/layer3");
            a_zone_params.put("element", "<member>"+_interfaceName+"</member>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_zone_params));

            return true;

        case DELETE:
            if (!managePrivateInterface(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS, privateVlanTag, privateGateway)) {
                return true;
            }

            // add cmds to the list
            // delete sub-interface from zone...
            Map<String, String> d_zone_params = new HashMap<String, String>();
            d_zone_params.put("type", "config");
            d_zone_params.put("action", "delete");
            d_zone_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/zone/entry[@name='"+_privateZone+"']/network/layer3/member[text()='"+_interfaceName+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_zone_params));

            // delete sub-interface from vsys...
            Map<String, String> d_vsys_params = new HashMap<String, String>();
            d_vsys_params.put("type", "config");
            d_vsys_params.put("action", "delete");
            d_vsys_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/import/network/interface/member[text()='"+_interfaceName+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_vsys_params));

            // delete sub-interface from VR...
            Map<String, String> d_vr_params = new HashMap<String, String>();
            d_vr_params.put("type", "config");
            d_vr_params.put("action", "delete");
            d_vr_params.put("xpath", "/config/devices/entry/network/virtual-router/entry[@name='"+_virtualRouter+"']/interface/member[text()='"+_interfaceName+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_vr_params));

            // delete sub-interface...
            Map<String, String> d_sub_params = new HashMap<String, String>();
            d_sub_params.put("type", "config");
            d_sub_params.put("action", "delete");
            d_sub_params.put("xpath", "/config/devices/entry/network/interface/"+_privateInterfaceType+"/entry[@name='"+_privateInterface+"']/layer3/units/entry[@name='"+_interfaceName+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_sub_params));

            return true;

        default:
            s_logger.debug("Unrecognized command.");
            return false;
        }
    }


    /*
     * Public Interfaces
     */

    private String genPublicInterfaceName(Long id) {
        return _publicInterface+"."+Long.toString(id);
    }

    public boolean managePublicInterface(ArrayList<IPaloAltoCommand> cmdList, PaloAltoPrimative prim, Long publicVlanTag, String publicIp, long privateVlanTag) throws ExecutionException {
        String _interfaceName = "";
        if (publicVlanTag == null) {
            _interfaceName = genPublicInterfaceName(new Long("9999"));
        } else {
            _interfaceName = genPublicInterfaceName(publicVlanTag);
        }

        switch (prim) {

        case CHECK_IF_EXISTS:
            // check if one exists already
            Map<String, String> params = new HashMap<String, String>();
            params.put("type", "config");
            params.put("action", "get");
            params.put("xpath", "/config/devices/entry/network/interface/"+_publicInterfaceType+"/entry[@name='"+_publicInterface+"']/layer3/units/entry[@name='"+_interfaceName+"']/ip/entry[@name='"+publicIp+"']");
            String response = request(PaloAltoMethod.GET, params);
            boolean result = (validResponse(response) && responseNotEmpty(response));
            s_logger.debug("Public sub-interface & IP exists: "+_interfaceName+" : "+publicIp+", "+result);
            return result;

        case ADD:
            if (managePublicInterface(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS, publicVlanTag, publicIp, privateVlanTag)) {
                return true;
            }

            // add IP to the sub-interface
            Map<String, String> a_sub_params = new HashMap<String, String>();
            a_sub_params.put("type", "config");
            a_sub_params.put("action", "set");
            a_sub_params.put("xpath", "/config/devices/entry/network/interface/"+_publicInterfaceType+"/entry[@name='"+_publicInterface+"']/layer3/units/entry[@name='"+_interfaceName+"']/ip");
            a_sub_params.put("element", "<entry name='"+publicIp+"'/>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_sub_params));

            // add sub-interface to VR (does nothing if already done)...
            Map<String, String> a_vr_params = new HashMap<String, String>();
            a_vr_params.put("type", "config");
            a_vr_params.put("action", "set");
            a_vr_params.put("xpath", "/config/devices/entry/network/virtual-router/entry[@name='"+_virtualRouter+"']/interface");
            a_vr_params.put("element", "<member>"+_interfaceName+"</member>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_vr_params));

            // add sub-interface to vsys (does nothing if already done)...
            Map<String, String> a_vsys_params = new HashMap<String, String>();
            a_vsys_params.put("type", "config");
            a_vsys_params.put("action", "set");
            a_vsys_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/import/network/interface");
            a_vsys_params.put("element", "<member>"+_interfaceName+"</member>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_vsys_params));

            // add sub-interface to zone (does nothing if already done)...
            Map<String, String> a_zone_params = new HashMap<String, String>();
            a_zone_params.put("type", "config");
            a_zone_params.put("action", "set");
            a_zone_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/zone/entry[@name='"+_publicZone+"']/network/layer3");
            a_zone_params.put("element", "<member>"+_interfaceName+"</member>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_zone_params));

            return true;

        case DELETE:
            if (!managePublicInterface(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS, publicVlanTag, publicIp, privateVlanTag)) {
                return true;
            }

            // delete IP from sub-interface...
            Map<String, String> d_sub_params = new HashMap<String, String>();
            d_sub_params.put("type", "config");
            d_sub_params.put("action", "delete");
            d_sub_params.put("xpath", "/config/devices/entry/network/interface/"+_publicInterfaceType+"/entry[@name='"+_publicInterface+"']/layer3/units/entry[@name='"+_interfaceName+"']/ip/entry[@name='"+publicIp+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_sub_params));

            return true;

        default:
            s_logger.debug("Unrecognized command.");
            return false;
        }
    }


    /*
     * Static NAT rules
     */



    /*
     * Destination NAT rules
     */



    /*
     * Source NAT rules
     */

    private String genSourceNatRuleName(Long privateVlanTag) {
        return "src_nat."+Long.toString(privateVlanTag);
    }

    public boolean manageSrcNatRule(ArrayList<IPaloAltoCommand> cmdList, PaloAltoPrimative prim, GuestNetworkType type, Long publicVlanTag, String publicIp, long privateVlanTag, String privateGateway) throws ExecutionException {
        String _publicInterfaceName = "";
        if (publicVlanTag == null) {
            _publicInterfaceName = genPublicInterfaceName(new Long("9999"));
        } else {
            _publicInterfaceName = genPublicInterfaceName(publicVlanTag);
        }
        String _srcNatName = genSourceNatRuleName(privateVlanTag);

        switch (prim) {

        case CHECK_IF_EXISTS:
            // check if one exists already
            Map<String, String> params = new HashMap<String, String>();
            params.put("type", "config");
            params.put("action", "get");
            params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/rulebase/nat/rules/entry[@name='"+_srcNatName+"']");
            String response = request(PaloAltoMethod.GET, params);
            boolean result = (validResponse(response) && responseNotEmpty(response));
            s_logger.debug("Source NAT exists: "+_srcNatName+", "+result);
            return result;

        case ADD:
            if (manageSrcNatRule(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS, type, publicVlanTag, publicIp, privateVlanTag, privateGateway)) {
                return true;
            }

            // add cmds
            // add source nat
            String xml = PaloAltoXml.SOURCE_NAT_ADD.getXml();                              
            xml = replaceXmlValue(xml, "from", _privateZone);
            xml = replaceXmlValue(xml, "to", _publicZone);
            xml = replaceXmlValue(xml, "source", privateGateway);
            xml = replaceXmlValue(xml, "destination", publicIp);
            xml = replaceXmlValue(xml, "to_interface", _publicInterfaceName);

            Map<String, String> a_params = new HashMap<String, String>();
            a_params.put("type", "config");
            a_params.put("action", "set");
            a_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/rulebase/nat/rules/entry[@name='"+_srcNatName+"']");
            a_params.put("element", xml);
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.POST, a_params));

            return true;

        case DELETE:
            if (!manageSrcNatRule(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS, type, publicVlanTag, publicIp, privateVlanTag, privateGateway)) {
                return true;
            }

            // add cmds to the list
            // remove source nat rule
            Map<String, String> d_params = new HashMap<String, String>();
            d_params.put("type", "config");
            d_params.put("action", "delete");
            d_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/rulebase/nat/rules/entry[@name='"+_srcNatName+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.POST, d_params));

            return true;

        default:
            s_logger.debug("Unrecognized command.");
            return false;
        }
    }


    
    /*
     * Security policies
     */



    /*
     * Usage    
     */

    private ExternalNetworkResourceUsageAnswer getUsageAnswer(ExternalNetworkResourceUsageCommand cmd) throws ExecutionException {
        try {   
            String socOpenException = "Failed to open a connection for Usage data.";
            String socCloseException = "Unable to close connection for Usage data.";
//            if (!openUsageSocket()) {
//                throw new ExecutionException(socOpenException);
//            }
 
            ExternalNetworkResourceUsageAnswer answer = new ExternalNetworkResourceUsageAnswer(cmd);

//            String xml = PaloAltoXml.FIREWALL_FILTER_BYTES_GETALL.getXml();
//            //String rawUsageData = sendUsageRequest(xml);        
//            Document doc = getDocument(rawUsageData);
//
//            NodeList counters = doc.getElementsByTagName("counter");
//            for (int i = 0; i < counters.getLength(); i++) {
//                Node n = counters.item(i);
//                if (n.getNodeName().equals("counter")) {
//                    NodeList counterInfoList = n.getChildNodes();
//                    String counterName = null;
//                    long byteCount = 0;
//
//                    for (int j = 0; j < counterInfoList.getLength(); j++) {
//                        Node counterInfo = counterInfoList.item(j);
//                        if (counterInfo.getNodeName().equals("counter-name")) {
//                            counterName = counterInfo.getFirstChild().getNodeValue();
//                        } else if (counterInfo.getNodeName().equals("byte-count")) {
//                            try {
//                                byteCount = Long.parseLong(counterInfo.getFirstChild().getNodeValue());
//                            } catch (Exception e) {
//                                s_logger.debug(e);
//                                byteCount = 0;
//                            }
//                        }                       
//                    }
//
//                    if (byteCount >= 0) {
//                        updateUsageAnswer(answer, counterName, byteCount);     
//                    }
//                } 
//            }
//            if (!closeUsageSocket()) {
//                throw new ExecutionException(socCloseException);
//            }
            return answer;
        } catch (Exception e) {
            //closeUsageSocket();
            throw new ExecutionException(e.getMessage());
        }

    }       

//    private void updateBytesMap(Map<String, long[]> bytesMap, UsageFilter filter, String usageAnswerKey, long additionalBytes) {
//        long[] bytesSentAndReceived = bytesMap.get(usageAnswerKey);     
//        if (bytesSentAndReceived == null) {
//            bytesSentAndReceived = new long[]{0,0};
//        }
//
//        int index = 0;
//        if (filter.equals(_usageFilterVlanOutput) || filter.equals(_usageFilterIPInput)) {
//            index = 1;
//        }
//
//        bytesSentAndReceived[index] += additionalBytes;
//        bytesMap.put(usageAnswerKey, bytesSentAndReceived);
//    }

//    private String getIpAddress(String counterName) {
//        String[] counterNameArray = counterName.split("-");
//
//        if (counterNameArray.length < 4) {
//            return null;
//        } else {
//            return counterNameArray[0] + "." + counterNameArray[1] + "." + counterNameArray[2] + "." + counterNameArray[3];
//        }
//    }

//    private String getGuestVlanTag(String counterName) {
//        String[] counterNameArray = counterName.split("-");
//
//        if (counterNameArray.length != 3) {
//            return null;
//        } else {
//            return counterNameArray[2];
//        }
//    }

//    private UsageFilter getUsageFilter(String counterName) {
//
//        if (counterName.contains(_usageFilterVlanInput.getCounterIdentifier())) {
//            return _usageFilterVlanInput;
//        } else if (counterName.contains(_usageFilterVlanOutput.getCounterIdentifier())) {
//            return _usageFilterVlanOutput;
//        } else if (counterName.contains(_usageFilterIPInput.getCounterIdentifier())) {
//            return _usageFilterIPInput;
//        } else if (counterName.contains(_usageFilterIPOutput.getCounterIdentifier())) {
//            return _usageFilterIPOutput;
//        } 
// 
//        return null;
//    }

//    private String getUsageAnswerKey(UsageFilter filter, String counterName) {
//        if (filter.equals(_usageFilterVlanInput) || filter.equals(_usageFilterVlanOutput)) {
//            return getGuestVlanTag(counterName);
//        } else if (filter.equals(_usageFilterIPInput) || filter.equals(_usageFilterIPOutput)) {
//            return getIpAddress(counterName);
//        } else {
//            return null;
//        } 
//    }

//    private Map<String, long[]> getBytesMap(ExternalNetworkResourceUsageAnswer answer, UsageFilter filter, String usageAnswerKey) {
//        if (filter.equals(_usageFilterVlanInput) || filter.equals(_usageFilterVlanOutput)) {
//            return answer.guestVlanBytes;
//        } else if (filter.equals(_usageFilterIPInput) || filter.equals(_usageFilterIPOutput)) {
//            return answer.ipBytes;
//        } else {
//            return null;
//        } 
//    }

//    private void updateUsageAnswer(ExternalNetworkResourceUsageAnswer answer, String counterName, long byteCount) {
//        if (counterName == null || byteCount <= 0) {
//            return;                   
//        }               
//
//        //UsageFilter filter = getUsageFilter(counterName);       
//        if (filter == null) {
//            s_logger.debug("Failed to parse counter name in usage answer: " + counterName);
//            return;
//        }
//        //String usageAnswerKey = getUsageAnswerKey(filter, counterName);     
//        //Map<String, long[]> bytesMap = getBytesMap(answer, filter, usageAnswerKey);
//        //updateBytesMap(bytesMap, filter, usageAnswerKey, byteCount);          
//    }


    /*
     * Helper config functions
     */
    public boolean managePingProfile(ArrayList<IPaloAltoCommand> cmdList, PaloAltoPrimative prim) throws ExecutionException {
        switch (prim) {

        case CHECK_IF_EXISTS:
            // check if one exists already
            Map<String, String> params = new HashMap<String, String>();
            params.put("type", "config");
            params.put("action", "get");
            params.put("xpath", "/config/devices/entry/network/profiles/interface-management-profile/entry[@name='"+_pingManagementProfile+"']");
            String response = request(PaloAltoMethod.GET, params);
            boolean result = (validResponse(response) && responseNotEmpty(response));
            s_logger.debug("Management profile exists: "+_pingManagementProfile+", "+result);
            return result;

        case ADD:
            if (managePingProfile(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS)) {
                return true;
            }

            // add ping profile...
            Map<String, String> a_params = new HashMap<String, String>();
            a_params.put("type", "config");
            a_params.put("action", "set");
            a_params.put("xpath", "/config/devices/entry/network/profiles/interface-management-profile/entry[@name='"+_pingManagementProfile+"']");
            a_params.put("element", "<ping>yes</ping>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_params));

            return true;

        case DELETE:
            if (!managePingProfile(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS)) {
                return true;
            }

            // delete ping profile...
            Map<String, String> d_params = new HashMap<String, String>();
            d_params.put("type", "config");
            d_params.put("action", "delete");
            d_params.put("xpath", "/config/devices/entry/network/profiles/interface-management-profile/entry[@name='"+_pingManagementProfile+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_params));

            return true;

        default:
            s_logger.debug("Unrecognized command.");
            return false;
        }
    }





    /*
     * XML API commands
     */

    /* Function to make calls to the Palo Alto API. */
    /* All API calls will end up going through this function. */
    private String request(PaloAltoMethod method, Map<String, String> params) throws ExecutionException {
        if (method != PaloAltoMethod.GET && method != PaloAltoMethod.POST) {
            throw new ExecutionException("Invalid http method used to access the Palo Alto API.");
        }

        String responseBody = "";
        String debug_msg = "Palo Alto Request\n";

        // a GET method...
        if (method == PaloAltoMethod.GET) {
            String queryString = "?";
            for (String key : params.keySet()) {
                if (!queryString.equals("?")) {
                    queryString = queryString + "&";
                }
                try {
                    queryString = queryString + key+"="+URLEncoder.encode(params.get(key), "UTF-8");
                } catch (UnsupportedEncodingException e) {
                    throw new ExecutionException(e.getMessage());
                }
            }
            if (_key != null) {
                queryString = queryString + "&key="+_key;
            }

            try {
                debug_msg = debug_msg + "GET request: https://" + _ip + _apiUri + URLDecoder.decode(queryString, "UTF-8") + "\n";
            } catch (UnsupportedEncodingException e) {
                debug_msg = debug_msg + "GET request: https://" + _ip + _apiUri + queryString + "\n";
            }
            

            HttpGet get_request = new HttpGet("https://" + _ip + _apiUri + queryString);
            ResponseHandler<String> responseHandler = new BasicResponseHandler();
            try {
                responseBody = _httpclient.execute(get_request, responseHandler);
            } catch (IOException e) {
                throw new ExecutionException(e.getMessage());
            }
        }

        // a POST method...
        if (method == PaloAltoMethod.POST) {
            List <NameValuePair> nvps = new ArrayList <NameValuePair>();
            for (String key : params.keySet()) {
                nvps.add(new BasicNameValuePair(key, params.get(key)));
            }
            if (_key != null) {
                nvps.add(new BasicNameValuePair("key", _key));
            }

            debug_msg = debug_msg + "POST request: https://" + _ip + _apiUri + "\n";
            for (NameValuePair nvp : nvps) {
                debug_msg = debug_msg + "param: "+nvp.getName()+", "+nvp.getValue() + "\n";
            }

            HttpPost post_request = new HttpPost("https://" + _ip + _apiUri);
            try {
                post_request.setEntity(new UrlEncodedFormEntity(nvps, HTTP.UTF_8));
            } catch (UnsupportedEncodingException e) {
                throw new ExecutionException(e.getMessage());
            }
            ResponseHandler<String> responseHandler = new BasicResponseHandler();
            try {
                responseBody = _httpclient.execute(post_request, responseHandler);
            } catch (IOException e) {
                throw new ExecutionException(e.getMessage());
            }
        }

        debug_msg = debug_msg + prettyFormat(responseBody);
        s_logger.debug(debug_msg);
        
        return responseBody;
    }
    
    /* Used for requests that require polling to get a result (eg: commit) */
    private String requestWithPolling(PaloAltoMethod method, Map<String, String> params) throws ExecutionException {
        String job_id;
        String job_response = request(method, params);
        Document doc = getDocument(job_response);
        XPath xpath = XPathFactory.newInstance().newXPath();
        try {
            XPathExpression expr = xpath.compile("/response[@status='success']/result/job/text()");
            job_id = (String) expr.evaluate(doc, XPathConstants.STRING);
        } catch (XPathExpressionException e) {
            throw new ExecutionException(e.getCause().getMessage());
        }
        if (job_id.length() > 0) {
            boolean finished = false;
            Map<String, String> job_params = new HashMap<String, String>();
            job_params.put("type", "op");
            job_params.put("cmd", "<show><jobs><id>"+job_id+"</id></jobs></show>");

            while (!finished) {
                String job_status;
                String response = request(PaloAltoMethod.GET, job_params);
                Document job_doc = getDocument(response);
                XPath job_xpath = XPathFactory.newInstance().newXPath();
                try {
                    XPathExpression expr = job_xpath.compile("/response[@status='success']/result/job/status/text()");
                    job_status = (String) expr.evaluate(job_doc, XPathConstants.STRING);
                } catch (XPathExpressionException e) {
                    throw new ExecutionException(e.getCause().getMessage());
                }
                if (job_status.equals("FIN")) {
                    finished = true;
                    String job_result;
                    try {
                        XPathExpression expr = job_xpath.compile("/response[@status='success']/result/job/result/text()");
                        job_result = (String) expr.evaluate(job_doc, XPathConstants.STRING);
                    } catch (XPathExpressionException e) {
                        throw new ExecutionException(e.getCause().getMessage());
                    }
                    if (!job_result.equals("OK")) {
                        NodeList job_details;
                        try {
                            XPathExpression expr = job_xpath.compile("/response[@status='success']/result/job/details/line");
                            job_details = (NodeList) expr.evaluate(job_doc, XPathConstants.NODESET);
                        } catch (XPathExpressionException e) {
                            throw new ExecutionException(e.getCause().getMessage());
                        }
                        String error = "";
                        for (int i = 0; i < job_details.getLength(); i++) {
                            error = error + job_details.item(i).getTextContent() + "\n";
                        }
                        throw new ExecutionException(error);
                    }
                    return response;
                } else {
                    try {
                        Thread.sleep(2000); // poll periodically for the status of the async job...
                    } catch (InterruptedException e) { /* do nothing */ }
                }
            }
        } else {
            return job_response;
        }
        return null;
    }

    /* Runs a sequence of commands and attempts to commit at the end. */
    /* Uses the Command pattern to enable overriding of the response handling if needed. */
    private synchronized boolean requestWithCommit(ArrayList<IPaloAltoCommand> commandList) throws ExecutionException {
        boolean result = true;

        if (commandList.size() > 0) {
            // CHECK IF THERE IS PENDING CHANGES THAT HAVE NOT BEEN COMMITTED...
            String pending_changes;
            Map<String, String> check_params = new HashMap<String, String>();
            check_params.put("type", "op");
            check_params.put("cmd", "<check><pending-changes></pending-changes></check>");
            String check_response = request(PaloAltoMethod.GET, check_params); 
            Document check_doc = getDocument(check_response);
            XPath check_xpath = XPathFactory.newInstance().newXPath();
            try {
                XPathExpression expr = check_xpath.compile("/response[@status='success']/result/text()");
                pending_changes = (String) expr.evaluate(check_doc, XPathConstants.STRING);
            } catch (XPathExpressionException e) {
                throw new ExecutionException(e.getCause().getMessage());
            }
            if (pending_changes.equals("yes")) {
                throw new ExecutionException("The Palo Alto has uncommited changes, so no changes can be made.  Try again later or contact your administrator.");
            } else {
                // ADD A CONFIG LOCK TO CAPTURE THE PALO ALTO RESOURCE
                String add_lock_status;
                Map<String, String> add_lock_params = new HashMap<String, String>();
                add_lock_params.put("type", "op");
                add_lock_params.put("cmd", "<request><config-lock><add></add></config-lock></request>");
                String add_lock_response = request(PaloAltoMethod.GET, add_lock_params); 
                Document add_lock_doc = getDocument(add_lock_response);
                XPath add_lock_xpath = XPathFactory.newInstance().newXPath();
                try {
                    XPathExpression expr = add_lock_xpath.compile("/response[@status='success']/result/text()");
                    add_lock_status = (String) expr.evaluate(add_lock_doc, XPathConstants.STRING);
                } catch (XPathExpressionException e) {
                    throw new ExecutionException(e.getCause().getMessage());
                }
                if (add_lock_status.length() == 0) {
                    throw new ExecutionException("The Palo Alto is locked, no changes can be made at this time.");
                }

                try {
                    // RUN THE SEQUENCE OF COMMANDS
                    for (IPaloAltoCommand command : commandList) {
                        result = (result && command.execute()); // run commands and modify result boolean
                    }

                    // COMMIT THE CHANGES (ALSO REMOVES CONFIG LOCK)
                    String commit_job_id;
                    Map<String, String> commit_params = new HashMap<String, String>();
                    commit_params.put("type", "commit");
                    commit_params.put("cmd", "<commit></commit>");
                    String commit_response = requestWithPolling(PaloAltoMethod.GET, commit_params);
                    Document commit_doc = getDocument(commit_response);
                    XPath commit_xpath = XPathFactory.newInstance().newXPath();
                    try {
                        XPathExpression expr = commit_xpath.compile("/response[@status='success']/result/job/id/text()");
                        commit_job_id = (String) expr.evaluate(commit_doc, XPathConstants.STRING);
                    } catch (XPathExpressionException e) {
                        throw new ExecutionException(e.getCause().getMessage());
                    }
                    if (commit_job_id.length() == 0) { // no commit was done, so release the lock...
                        // REMOVE THE CONFIG LOCK TO RELEASE THE PALO ALTO RESOURCE
                        String remove_lock_status;
                        Map<String, String> remove_lock_params = new HashMap<String, String>();
                        remove_lock_params.put("type", "op");
                        remove_lock_params.put("cmd", "<request><config-lock><remove></remove></config-lock></request>");
                        String remove_lock_response = request(PaloAltoMethod.GET, remove_lock_params); 
                        Document remove_lock_doc = getDocument(remove_lock_response);
                        XPath remove_lock_xpath = XPathFactory.newInstance().newXPath();
                        try {
                            XPathExpression expr = remove_lock_xpath.compile("/response[@status='success']/result/text()");
                            remove_lock_status = (String) expr.evaluate(remove_lock_doc, XPathConstants.STRING);
                        } catch (XPathExpressionException e) {
                            throw new ExecutionException(e.getCause().getMessage());
                        }
                        if (remove_lock_status.length() == 0) {
                            throw new ExecutionException("Could not release the Palo Alto device.  Please notify an administrator!");
                        }
                    }
                    
                } catch (ExecutionException ex) {
                    // REVERT TO RUNNING
                    String revert_job_id;
                    Map<String, String> revert_params = new HashMap<String, String>();
                    revert_params.put("type", "op");
                    revert_params.put("cmd", "<load><config><from>running-config.xml</from></config></load>");
                    requestWithPolling(PaloAltoMethod.GET, revert_params);

                    // REMOVE THE CONFIG LOCK TO RELEASE THE PALO ALTO RESOURCE
                    String remove_lock_status;
                    Map<String, String> remove_lock_params = new HashMap<String, String>();
                    remove_lock_params.put("type", "op");
                    remove_lock_params.put("cmd", "<request><config-lock><remove></remove></config-lock></request>");
                    String remove_lock_response = request(PaloAltoMethod.GET, remove_lock_params); 
                    Document remove_lock_doc = getDocument(remove_lock_response);
                    XPath remove_lock_xpath = XPathFactory.newInstance().newXPath();
                    try {
                        XPathExpression expr = remove_lock_xpath.compile("/response[@status='success']/result/text()");
                        remove_lock_status = (String) expr.evaluate(remove_lock_doc, XPathConstants.STRING);
                    } catch (XPathExpressionException e) {
                        throw new ExecutionException(e.getCause().getMessage());
                    }
                    if (remove_lock_status.length() == 0) {
                        throw new ExecutionException("Could not release the Palo Alto device.  Please notify an administrator!");
                    }

                    throw ex; // Bubble up the reason we reverted...
                }

                return result;
            }
        } else {
            return true; // nothing to do
        }
    }

    /* A default response handler to validate that the request was successful. */
    public boolean validResponse(String response) throws ExecutionException {
        NodeList response_body;
        Document doc = getDocument(response);
        XPath xpath = XPathFactory.newInstance().newXPath();
        try {
            XPathExpression expr = xpath.compile("/response[@status='success']");
            response_body = (NodeList) expr.evaluate(doc, XPathConstants.NODESET);
        } catch (XPathExpressionException e) {
            throw new ExecutionException(e.getCause().getMessage());
        }

        if (response_body.getLength() > 0) {
            return true;
        } else {
            NodeList error_details;
            try {
                XPathExpression expr = xpath.compile("/response/msg/line/line");
                error_details = (NodeList) expr.evaluate(doc, XPathConstants.NODESET);
            } catch (XPathExpressionException e) {
                throw new ExecutionException(e.getCause().getMessage());
            }
            if (error_details.getLength() == 0) {
                try {
                    XPathExpression expr = xpath.compile("/response/msg/line");
                    error_details = (NodeList) expr.evaluate(doc, XPathConstants.NODESET);
                } catch (XPathExpressionException e) {
                    throw new ExecutionException(e.getCause().getMessage());
                }

                if (error_details.getLength() == 0) {
                    try {
                        XPathExpression expr = xpath.compile("/response/result/msg");
                        error_details = (NodeList) expr.evaluate(doc, XPathConstants.NODESET);
                    } catch (XPathExpressionException e) {
                        throw new ExecutionException(e.getCause().getMessage());
                    }
                }
            }
            String error = "";
            for (int i = 0; i < error_details.getLength(); i++) {
                error = error + error_details.item(i).getTextContent() + "\n";
            }
            throw new ExecutionException(error);
        }
    }

    /* Validate that the response is not empty. */
    public boolean responseNotEmpty(String response) throws ExecutionException {
        NodeList response_body;
        Document doc = getDocument(response);
        XPath xpath = XPathFactory.newInstance().newXPath();
        try {
            XPathExpression expr = xpath.compile("/response[@status='success']");
            response_body = (NodeList) expr.evaluate(doc, XPathConstants.NODESET);
        } catch (XPathExpressionException e) {
            throw new ExecutionException(e.getCause().getMessage());
        }

        if (response_body.getLength() > 0 && 
            (!response_body.item(0).getTextContent().equals("") || 
                (response_body.item(0).hasChildNodes() && response_body.item(0).getFirstChild().hasChildNodes()))) {
            return true;
        } else {
            return false;
        }
    }

    /* Get the type of interface from the PA device. */
    private String getInterfaceType(String interface_name) throws ExecutionException {
        String[] types = { InterfaceType.ETHERNET.toString(), InterfaceType.AGGREGATE.toString() };
        for (String type : types) {
            Map<String, String> params = new HashMap<String, String>();
            params.put("type", "config");
            params.put("action", "get");
            params.put("xpath", "/config/devices/entry/network/interface/"+type+"/entry[@name='"+interface_name+"']");
            String ethernet_response = request(PaloAltoMethod.GET, params);
            if (validResponse(ethernet_response) && responseNotEmpty(ethernet_response)) {
                return type;
            }
        }
        return "";
    }


    /* Command Interface */
    public interface IPaloAltoCommand {
        public boolean execute() throws ExecutionException;
    }

    /* Command Abstract */
    private abstract class AbstractPaloAltoCommand implements IPaloAltoCommand {
        PaloAltoMethod method;
        Map<String, String> params;
        
        public AbstractPaloAltoCommand() {}

        public AbstractPaloAltoCommand(PaloAltoMethod method, Map<String, String> params) {
            this.method = method;
            this.params = params;
        }

        public boolean execute() throws ExecutionException {
            String response = request(method, params); 
            return validResponse(response);
        }
    }

    /* Implement the default functionality */
    private class DefaultPaloAltoCommand extends AbstractPaloAltoCommand {
        public DefaultPaloAltoCommand(PaloAltoMethod method, Map<String, String> params) {
            super(method, params);
        }
    }



    /*
     * XML utils
     */

    private String replaceXmlValue(String xml, String marker, String value) {
        marker = "\\s*%" + marker + "%\\s*";

        if (value == null) {
            value = "";
        }

        return xml.replaceAll(marker, value);
    }


    /*
     * Misc
     */    
    
    private String genIpIdentifier(String ip) {
        return ip.replace('.', '-').replace('/', '-');
    }

    private Protocol getProtocol(String protocolName) throws ExecutionException {
        protocolName = protocolName.toLowerCase();

        try {
            return Protocol.valueOf(protocolName);
        } catch (Exception e) {
            throw new ExecutionException("Invalid protocol: " + protocolName);
        }       
    }

    private Document getDocument(String xml) throws ExecutionException {
        StringReader xmlReader = new StringReader(xml);
        InputSource xmlSource = new InputSource(xmlReader);
        Document doc = null; 

        try {
            doc = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(xmlSource);
        } catch (Exception e) {
            s_logger.error(e);
            throw new ExecutionException(e.getMessage());
        }

        if (doc == null) {
            throw new ExecutionException("Failed to parse xml " + xml);
        } else {
            return doc;
        }
    }

    private String prettyFormat(String input) {
        try {
            Source xmlInput = new StreamSource(new StringReader(input));
            StringWriter stringWriter = new StringWriter();
            StreamResult xmlOutput = new StreamResult(stringWriter);
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            transformerFactory.setAttribute("indent-number", 4);
            Transformer transformer = transformerFactory.newTransformer(); 
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
            transformer.transform(xmlInput, xmlOutput);
            return xmlOutput.getWriter().toString();
        } catch (Exception e) {
            return "prettyFormat() could not reformat the XML string.";
        }
    }

    private String uuidToBase64(String str) {
        Base64 base64 = new Base64();
        UUID uuid = UUID.fromString(str);
        ByteBuffer bb = ByteBuffer.wrap(new byte[16]);
        bb.putLong(uuid.getMostSignificantBits());
        bb.putLong(uuid.getLeastSignificantBits());
        return base64.encodeBase64URLSafeString(bb.array());
    }

    private String uuidFromBase64(String str) {
        Base64 base64 = new Base64(); 
        byte[] bytes = base64.decodeBase64(str);
        ByteBuffer bb = ByteBuffer.wrap(bytes);
        UUID uuid = new UUID(bb.getLong(), bb.getLong());
        return uuid.toString();
    }

    //@Override
    public void setName(String name) {
        // TODO Auto-generated method stub
        
    }

    //@Override
    public void setConfigParams(Map<String, Object> params) {
        // TODO Auto-generated method stub
        
    }

    //@Override
    public Map<String, Object> getConfigParams() {
        // TODO Auto-generated method stub
        return null;
    }

    //@Override
    public int getRunLevel() {
        // TODO Auto-generated method stub
        return 0;
    }

    //@Override
    public void setRunLevel(int level) {
        // TODO Auto-generated method stub
        
    }    
    
}
