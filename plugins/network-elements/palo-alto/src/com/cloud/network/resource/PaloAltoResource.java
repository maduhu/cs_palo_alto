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
    private PrintWriter _toPaloAlto;
    private BufferedReader _fromPaloAlto;
    private PrintWriter _UsagetoPaloAlto;
    private BufferedReader _UsagefromPaloAlto;
    private Integer _numRetries;
    private Integer _timeoutInSeconds;
    private String _publicZone;
    private String _privateZone;
//    private String _publicZoneInputFilterName;
    private String _publicInterface;
    private String _privateInterface;
    private String _publicInterfaceType;
    private String _privateInterfaceType;
    private String _virtualRouter;
    private String _usageInterface;
//    private String _ikeProposalName;
//    private String _ipsecPolicyName;
//    private String _primaryDnsAddress;
//    private String _ikeGatewayHostname;
//    private String _vpnObjectPrefix;
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

//    public class FirewallFilterTerm {
//        private String name;
//        private List<String> sourceCidrs;
//        private String destIp;
//        private String portRange;
//        private String protocol;
//        private String icmpType;
//        private String icmpCode;
//        private String countName;
//        
//        private FirewallFilterTerm(String name, List<String> sourceCidrs, String destIp, String protocol, Integer startPort, Integer endPort,
//                Integer icmpType, Integer icmpCode, String countName) {
//            this.name = name;
//            this.sourceCidrs = sourceCidrs;
//            this.destIp = destIp;
//            this.protocol = protocol;
//            
//            if (protocol.equals("tcp") || protocol.equals("udp")) {
//                this.portRange = String.valueOf(startPort) + "-" + String.valueOf(endPort);
//            } else if (protocol.equals("icmp")) {
//                this.icmpType = String.valueOf(icmpType);
//                this.icmpCode = String.valueOf(icmpCode);
//            } else {
//                assert protocol.equals("any");
//            }
//            this.countName = countName;
//            
//        }
//
//        public String getName() {
//            return name;
//        }
//        
//        public List<String> getSourceCidrs() {
//            return sourceCidrs;
//        }
//        
//        public String getDestIp() {
//            return destIp;
//        }
//        
//        public String getPortRange() {
//            return portRange;
//        }
//        
//        public String getProtocol() {
//            return protocol;
//        }
//        
//        public String getIcmpType() {
//            return icmpType;
//        }
//        
//        public String getIcmpCode() {
//            return icmpCode;
//        }
//        
//        public String getCountName() {
//            return countName;
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


//    /*
//     * The usage data will be handled on it's own socket, so usage 
//     * commands will use the following methods...
//     */
//    private boolean usageLogin() throws ExecutionException {
//        String xml = PaloAltoXml.LOGIN.getXml();
//        xml = replaceXmlValue(xml, "username", _username);
//        xml = replaceXmlValue(xml, "password", _password);
//        return sendUsageRequestAndCheckResponse(PaloAltoPrimative.LOGIN, xml);
//    }
//
//    
//    private boolean openUsageSocket() throws ExecutionException {
//        try {
//            Socket s = new Socket(_ip, 3221);
//            s.setKeepAlive(true);
//            s.setSoTimeout(_timeoutInSeconds * 1000);
//            _UsagetoPaloAlto = new PrintWriter(s.getOutputStream(), true);
//            _UsagefromPaloAlto = new BufferedReader(new InputStreamReader(s.getInputStream()));
//            return usageLogin();
//        } catch (IOException e) {
//            s_logger.error(e);
//            return false;
//        }
//    }
//    
//    private boolean closeUsageSocket() {
//        try {
//            if (_UsagetoPaloAlto != null) {
//                _UsagetoPaloAlto.close();
//            } 
//
//            if (_UsagefromPaloAlto != null) {
//                _UsagefromPaloAlto.close();
//            }
//
//            return true;
//        } catch (IOException e) {
//            s_logger.error(e);
//            return false;
//        }
//    }
//    
//    /*
//     * Commit/rollback
//     */
//
//    private void openConfiguration() throws ExecutionException {
//        String xml = PaloAltoXml.OPEN_CONFIGURATION.getXml();
//        String successMsg = "Opened a private configuration.";
//        String errorMsg = "Failed to open a private configuration.";
//
//        if (!sendRequestAndCheckResponse(PaloAltoPrimative.OPEN_CONFIGURATION, xml)) {
//            throw new ExecutionException(errorMsg);
//        } else {
//            s_logger.debug(successMsg);
//        }
//    }
//
//    private void closeConfiguration() {
//        String xml = PaloAltoXml.CLOSE_CONFIGURATION.getXml();
//        String successMsg = "Closed private configuration.";
//        String errorMsg = "Failed to close private configuration.";
//
//        try {
//            if (!sendRequestAndCheckResponse(PaloAltoPrimative.CLOSE_CONFIGURATION, xml)) {
//                s_logger.error(errorMsg);
//            } 
//        } catch (ExecutionException e) {
//            s_logger.error(errorMsg);
//        }
//
//        s_logger.debug(successMsg);
//    }
//
//    private void commitConfiguration() throws ExecutionException {
//        String xml = PaloAltoXml.COMMIT.getXml();
//        String successMsg = "Committed to global configuration.";
//        String errorMsg = "Failed to commit to global configuration.";
//
//        if (!sendRequestAndCheckResponse(PaloAltoPrimative.COMMIT, xml)) {
//            throw new ExecutionException(errorMsg);
//        } else {            
//            s_logger.debug(successMsg);
//            closeConfiguration();
//        }
//    }

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
            shutdownGuestNetwork(commandList, type, ip.getAccountId(), publicVlanTag, sourceNatIpAddress, guestVlanTag, guestVlanGateway, guestVlanSubnet, cidrSize);
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
            manageNatRule(cmdList, PaloAltoPrimative.ADD, type, publicVlanTag, publicIp, privateVlanTag, privateGateway);         
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

    private void shutdownGuestNetwork(ArrayList<IPaloAltoCommand> cmdList, GuestNetworkType type, long accountId, Long publicVlanTag, String sourceNatIpAddress, long privateVlanTag, String privateGateway, String privateSubnet, long privateCidrSize) throws ExecutionException {     
        // Remove static and destination NAT rules for the guest network
        //removeStaticAndDestNatRulesInPrivateVlan(privateVlanTag, privateGateway, privateCidrSize);

        privateGateway = privateGateway + "/" + privateCidrSize;
        privateSubnet = privateSubnet + "/" + privateCidrSize;

        if (sourceNatIpAddress != null) {
            sourceNatIpAddress = sourceNatIpAddress+"/32";
        }

        if (type.equals(GuestNetworkType.SOURCE_NAT)) {
            manageNatRule(cmdList, PaloAltoPrimative.DELETE, type, publicVlanTag, sourceNatIpAddress, privateVlanTag, privateGateway);
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

    



    /* security policies */
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
     * General NAT utils
     */
    
//    private List<String[]> getAllStaticAndDestNatRules() throws ExecutionException {
//        List<String[]> staticAndDestNatRules = new ArrayList<String[]>(); 
//        //staticAndDestNatRules.addAll(getStaticNatRules(RuleMatchCondition.ALL, null, null));
//        //staticAndDestNatRules.addAll(getDestNatRules(RuleMatchCondition.ALL, null, null, null, null));      
//        return staticAndDestNatRules;
//    }  
    
//    private void removeStaticAndDestNatRulesInPrivateVlan(long privateVlanTag, String privateGateway, long privateCidrSize) throws ExecutionException {
//        List<String[]> staticNatRulesToRemove = getStaticNatRules(RuleMatchCondition.PRIVATE_SUBNET, privateGateway, privateCidrSize);
//        List<String[]> destNatRulesToRemove = getDestNatRules(RuleMatchCondition.PRIVATE_SUBNET, null, null, privateGateway, privateCidrSize);
//        
//        List<String> publicIps = new ArrayList<String>();
//        addPublicIpsToList(staticNatRulesToRemove, publicIps);
//        addPublicIpsToList(destNatRulesToRemove, publicIps);
//        
//        Map<String, Long> publicVlanTags = getPublicVlanTagsForPublicIps(publicIps);
//        
//        removeStaticNatRules(privateVlanTag, publicVlanTags, staticNatRulesToRemove);
//        removeDestinationNatRules(privateVlanTag, publicVlanTags, destNatRulesToRemove);
//    }            

//    private Map<String, ArrayList<FirewallRuleTO>> getActiveRules(FirewallRuleTO[] allRules) {
//        Map<String, ArrayList<FirewallRuleTO>> activeRules = new HashMap<String, ArrayList<FirewallRuleTO>>();
//
//        for (FirewallRuleTO rule : allRules) {
//            String ipPair;
//
//            if (rule.getPurpose().equals(Purpose.StaticNat)) {
//                StaticNatRuleTO staticNatRule = (StaticNatRuleTO) rule;
//                ipPair = staticNatRule.getSrcIp() + "-" + staticNatRule.getDstIp();
//            } else if (rule.getPurpose().equals(Purpose.PortForwarding)) {
//                PortForwardingRuleTO portForwardingRule = (PortForwardingRuleTO) rule;
//                ipPair = portForwardingRule.getSrcIp() + "-" + portForwardingRule.getDstIp();
//            } else {
//                continue;
//            }
//
//            ArrayList<FirewallRuleTO> activeRulesForIpPair = activeRules.get(ipPair);
//
//            if (activeRulesForIpPair == null) {
//                activeRulesForIpPair = new ArrayList<FirewallRuleTO>();
//            }
//
//            if (!rule.revoked() || rule.isAlreadyAdded()) {
//                activeRulesForIpPair.add(rule);
//            }
//
//            activeRules.put(ipPair, activeRulesForIpPair);
//        }
//
//        return activeRules;
//    }
    
//    private Map<String, String> getVlanTagMap(FirewallRuleTO[] allRules) {
//        Map<String, String> vlanTagMap = new HashMap<String, String>();
//        
//        for (FirewallRuleTO rule : allRules) {
//            vlanTagMap.put(rule.getSrcIp(), rule.getSrcVlanTag());
//        }
//        
//        return vlanTagMap;
//    }
    

    /*
     * Private interfaces
     */

    private String genPrivateInterfaceName(long vlanTag) {
        return _privateInterface+"."+Long.toString(vlanTag);
    }

    public boolean managePrivateInterface(ArrayList<IPaloAltoCommand> cmdList, PaloAltoPrimative prim, long privateVlanTag, String privateGateway) throws ExecutionException {
        String _private_entry_name =  genPrivateInterfaceName(privateVlanTag);

        switch (prim) {

        case CHECK_IF_EXISTS:
            // check if one exists already
            Map<String, String> params = new HashMap<String, String>();
            params.put("type", "config");
            params.put("action", "get");
            params.put("xpath", "/config/devices/entry/network/interface/"+_privateInterfaceType+"/entry[@name='"+_privateInterface+"']/layer3/units/entry[@name='"+_private_entry_name+"']");
            String response = request(PaloAltoMethod.GET, params);
            boolean result = (validResponse(response) && responseNotEmpty(response));
            s_logger.debug("Private sub-interface exists: "+_private_entry_name+", "+result);
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
            a_sub_params.put("xpath", "/config/devices/entry/network/interface/"+_privateInterfaceType+"/entry[@name='"+_privateInterface+"']/layer3/units/entry[@name='"+_private_entry_name+"']");
            a_sub_params.put("element", "<tag>"+privateVlanTag+"</tag><ip><entry name='"+privateGateway+"'/></ip>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_sub_params));

            // add sub-interface to VR...
            Map<String, String> a_vr_params = new HashMap<String, String>();
            a_vr_params.put("type", "config");
            a_vr_params.put("action", "set");
            a_vr_params.put("xpath", "/config/devices/entry/network/virtual-router/entry[@name='"+_virtualRouter+"']/interface");
            a_vr_params.put("element", "<member>"+_private_entry_name+"</member>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_vr_params));

            // add sub-interface to vsys...
            Map<String, String> a_vsys_params = new HashMap<String, String>();
            a_vsys_params.put("type", "config");
            a_vsys_params.put("action", "set");
            a_vsys_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/import/network/interface");
            a_vsys_params.put("element", "<member>"+_private_entry_name+"</member>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_vsys_params));

            // add sub-interface to zone...
            Map<String, String> a_zone_params = new HashMap<String, String>();
            a_zone_params.put("type", "config");
            a_zone_params.put("action", "set");
            a_zone_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/zone/entry[@name='"+_privateZone+"']/network/layer3");
            a_zone_params.put("element", "<member>"+_private_entry_name+"</member>");
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
            d_zone_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/zone/entry[@name='"+_privateZone+"']/network/layer3/member[text()='"+_private_entry_name+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_zone_params));

            // delete sub-interface from vsys...
            Map<String, String> d_vsys_params = new HashMap<String, String>();
            d_vsys_params.put("type", "config");
            d_vsys_params.put("action", "delete");
            d_vsys_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/import/network/interface/member[text()='"+_private_entry_name+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_vsys_params));

            // delete sub-interface from VR...
            Map<String, String> d_vr_params = new HashMap<String, String>();
            d_vr_params.put("type", "config");
            d_vr_params.put("action", "delete");
            d_vr_params.put("xpath", "/config/devices/entry/network/virtual-router/entry[@name='"+_virtualRouter+"']/interface/member[text()='"+_private_entry_name+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_vr_params));

            // delete sub-interface...
            Map<String, String> d_sub_params = new HashMap<String, String>();
            d_sub_params.put("type", "config");
            d_sub_params.put("action", "delete");
            d_sub_params.put("xpath", "/config/devices/entry/network/interface/"+_privateInterfaceType+"/entry[@name='"+_privateInterface+"']/layer3/units/entry[@name='"+_private_entry_name+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_sub_params));

            return true;

        default:
            s_logger.debug("Unrecognized command.");
            return false;
        }
    }
    
//    private Long getVlanTagFromInterfaceName(String interfaceName) throws ExecutionException {
//        Long vlanTag = null;
//        
//        if (interfaceName.contains(".")) {
//            try {
//                String unitNum = interfaceName.split("\\.")[1];
//                if (!unitNum.equals("0")) {
//                    vlanTag = Long.parseLong(unitNum);
//                }
//            } catch (Exception e) {
//                s_logger.error(e);
//                throw new ExecutionException("Unable to parse VLAN tag from interface name: " + interfaceName);
//            }
//        }
//    
//        return vlanTag;
//    }


    /*
     * Public Interfaces
     */

    private String genPublicInterfaceName(String publicIp) {
        return _publicInterface+"."+genIpIdentifier(publicIp);
    }

    public boolean managePublicInterface(ArrayList<IPaloAltoCommand> cmdList, PaloAltoPrimative prim, Long publicVlanTag, String publicIp, long privateVlanTag) throws ExecutionException {
        String _public_entry_name = genPublicInterfaceName(publicIp);

        switch (prim) {

        case CHECK_IF_EXISTS:
            // check if one exists already
            Map<String, String> params = new HashMap<String, String>();
            params.put("type", "config");
            params.put("action", "get");
            params.put("xpath", "/config/devices/entry/network/interface/"+_publicInterfaceType+"/entry[@name='"+_publicInterface+"']/layer3/units/entry[@name='"+_public_entry_name+"']");
            String response = request(PaloAltoMethod.GET, params);
            boolean result = (validResponse(response) && responseNotEmpty(response));
            s_logger.debug("Public sub-interface exists: "+_public_entry_name+", "+result);
            return result;

        case ADD:
            if (managePublicInterface(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS, publicVlanTag, publicIp, privateVlanTag)) {
                return true;
            }

            // add cmds
            // add sub-interface
            Map<String, String> a_sub_params = new HashMap<String, String>();
            a_sub_params.put("type", "config");
            a_sub_params.put("action", "set");
            a_sub_params.put("xpath", "/config/devices/entry/network/interface/"+_publicInterfaceType+"/entry[@name='"+_publicInterface+"']/layer3/units/entry[@name='"+_public_entry_name+"']");
            a_sub_params.put("element", "<ip><entry name='"+publicIp+"'/></ip>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_sub_params));

            // add sub-interface to VR...
            Map<String, String> a_vr_params = new HashMap<String, String>();
            a_vr_params.put("type", "config");
            a_vr_params.put("action", "set");
            a_vr_params.put("xpath", "/config/devices/entry/network/virtual-router/entry[@name='"+_virtualRouter+"']/interface");
            a_vr_params.put("element", "<member>"+_public_entry_name+"</member>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_vr_params));

            // add sub-interface to vsys...
            Map<String, String> a_vsys_params = new HashMap<String, String>();
            a_vsys_params.put("type", "config");
            a_vsys_params.put("action", "set");
            a_vsys_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/import/network/interface");
            a_vsys_params.put("element", "<member>"+_public_entry_name+"</member>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_vsys_params));

            // add sub-interface to zone...
            Map<String, String> a_zone_params = new HashMap<String, String>();
            a_zone_params.put("type", "config");
            a_zone_params.put("action", "set");
            a_zone_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/zone/entry[@name='"+_publicZone+"']/network/layer3");
            a_zone_params.put("element", "<member>"+_public_entry_name+"</member>");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, a_zone_params));

            return true;

        case DELETE:
            if (!managePublicInterface(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS, publicVlanTag, publicIp, privateVlanTag)) {
                return true;
            }

            // add cmds to the list
            // delete sub-interface from zone...
            Map<String, String> d_zone_params = new HashMap<String, String>();
            d_zone_params.put("type", "config");
            d_zone_params.put("action", "delete");
            d_zone_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/zone/entry[@name='"+_publicZone+"']/network/layer3/member[text()='"+_public_entry_name+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_zone_params));

            // delete sub-interface from vsys...
            Map<String, String> d_vsys_params = new HashMap<String, String>();
            d_vsys_params.put("type", "config");
            d_vsys_params.put("action", "delete");
            d_vsys_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/import/network/interface/member[text()='"+_public_entry_name+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_vsys_params));

            // delete sub-interface from VR...
            Map<String, String> d_vr_params = new HashMap<String, String>();
            d_vr_params.put("type", "config");
            d_vr_params.put("action", "delete");
            d_vr_params.put("xpath", "/config/devices/entry/network/virtual-router/entry[@name='"+_virtualRouter+"']/interface/member[text()='"+_public_entry_name+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_vr_params));

            // delete sub-interface...
            Map<String, String> d_sub_params = new HashMap<String, String>();
            d_sub_params.put("type", "config");
            d_sub_params.put("action", "delete");
            d_sub_params.put("xpath", "/config/devices/entry/network/interface/"+_publicInterfaceType+"/entry[@name='"+_publicInterface+"']/layer3/units/entry[@name='"+_public_entry_name+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.GET, d_sub_params));

            return true;

        default:
            s_logger.debug("Unrecognized command.");
            return false;
        }
    }



//    /*
//     * Proxy ARP
//     */
//
//    private boolean manageProxyArp(PaloAltoPrimative command, Long publicVlanTag, String publicIp) throws ExecutionException {
//        String publicInterface = genPublicInterface(publicVlanTag);
//        String xml;
//
//        switch (command) {
//
//        case CHECK_IF_EXISTS:
//            xml = PaloAltoXml.PROXY_ARP_GETONE.getXml();
//            xml = setDelete(xml, false);
//            xml = replaceXmlValue(xml, "public-interface-name", publicInterface);
//            xml = replaceXmlValue(xml, "public-ip-address", publicIp);
//            return sendRequestAndCheckResponse(command, xml, "name", publicIp + "/32");
//
//        case CHECK_IF_IN_USE:
//            // Check if any NAT rules are using this proxy ARP entry
//            String poolName = genSourceNatPoolName(publicIp);
//               
//            String allStaticNatRules = sendRequest(PaloAltoXml.STATIC_NAT_RULE_GETALL.getXml());
//            String allDestNatRules = sendRequest(replaceXmlValue(PaloAltoXml.DEST_NAT_RULE_GETALL.getXml(), "rule-set", _publicZone));
//            String allSrcNatRules = sendRequest(PaloAltoXml.SRC_NAT_RULE_GETALL.getXml());
//    
//            return (allStaticNatRules.contains(publicIp) ||
//                    allDestNatRules.contains(publicIp) ||
//                    allSrcNatRules.contains(poolName));
//
//        case ADD:
//            if (manageProxyArp(PaloAltoPrimative.CHECK_IF_EXISTS, publicVlanTag, publicIp)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.PROXY_ARP_ADD.getXml();
//            xml = replaceXmlValue(xml, "public-interface-name", publicInterface);
//            xml = replaceXmlValue(xml, "public-ip-address", publicIp);
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to add proxy ARP entry for public IP " + publicIp);
//            } else {
//                return true;
//            }
//
//        case DELETE:
//            if (!manageProxyArp(PaloAltoPrimative.CHECK_IF_EXISTS, publicVlanTag, publicIp)) {
//                return true;
//            }
//
//            if (manageProxyArp(PaloAltoPrimative.CHECK_IF_IN_USE, publicVlanTag, publicIp)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.PROXY_ARP_GETONE.getXml();
//            xml = setDelete(xml, true);
//            xml = replaceXmlValue(xml, "public-interface-name", publicInterface);
//            xml = replaceXmlValue(xml, "public-ip-address", publicIp);
//
//            if (!sendRequestAndCheckResponse(command, xml, "name", publicIp)) {
//                throw new ExecutionException("Failed to delete proxy ARP entry for public IP " + publicIp);
//            } else {
//                return true;
//            }
//
//        default:
//            s_logger.debug("Unrecognized command.");
//            return false;
//
//        }
//
//    }

//    private Map<String, Long> getPublicVlanTagsForPublicIps(List<String> publicIps) throws ExecutionException {
//        Map<String, Long> publicVlanTags = new HashMap<String, Long>();
//
//        List<String> interfaceNames = new ArrayList<String>();
//        
//        String xmlRequest = PaloAltoXml.PROXY_ARP_GETALL.getXml();
//        xmlRequest = replaceXmlValue(xmlRequest, "interface-name", "");
//        String xmlResponse = sendRequest(xmlRequest);       
//
//        Document doc = getDocument(xmlResponse);
//        NodeList interfaces = doc.getElementsByTagName("interface");
//        for (int i = 0; i < interfaces.getLength(); i++) {
//            String interfaceName = null;
//            NodeList interfaceEntries = interfaces.item(i).getChildNodes();               
//            for (int j = 0; j < interfaceEntries.getLength(); j++) {
//                Node interfaceEntry = interfaceEntries.item(j);
//                if (interfaceEntry.getNodeName().equals("name")) {
//                    interfaceName = interfaceEntry.getFirstChild().getNodeValue();
//                    break;
//                } 
//            }
//            
//            if (interfaceName != null) {
//                interfaceNames.add(interfaceName);
//            }
//        }
//        
//        if (interfaceNames.size() == 1) {
//            populatePublicVlanTagsMap(xmlResponse, interfaceNames.get(0), publicIps, publicVlanTags);
//        } else if (interfaceNames.size() > 1) {
//            for (String interfaceName : interfaceNames) {
//                xmlRequest = PaloAltoXml.PROXY_ARP_GETALL.getXml();
//                xmlRequest = replaceXmlValue(xmlRequest, "interface-name", interfaceName);
//                xmlResponse = sendRequest(xmlRequest);
//                populatePublicVlanTagsMap(xmlResponse, interfaceName, publicIps, publicVlanTags);
//            }
//        }
//        
//        return publicVlanTags;
//    }
    
//    private void populatePublicVlanTagsMap(String xmlResponse, String interfaceName, List<String> publicIps, Map<String, Long> publicVlanTags) throws ExecutionException {
//        Long publicVlanTag = getVlanTagFromInterfaceName(interfaceName);
//        if (publicVlanTag != null) {
//            for (String publicIp : publicIps) {
//                if (xmlResponse.contains(publicIp)) {
//                    publicVlanTags.put(publicIp, publicVlanTag);
//                }
//            }
//        }
//    }
    
//    private Map<String, Long> getPublicVlanTagsForNatRules(List<String[]> natRules) throws ExecutionException {
//        List<String> publicIps = new ArrayList<String>();
//        addPublicIpsToList(natRules, publicIps);
//        return getPublicVlanTagsForPublicIps(publicIps);
//    }
    
//    private void addPublicIpsToList(List<String[]> natRules, List<String> publicIps) {
//        for (String[] natRule : natRules) {
//            if (!publicIps.contains(natRule[0])) {
//                publicIps.add(natRule[0]);
//            }
//        }
//    }
    
//    private String genPublicInterface(Long vlanTag) {
//        String publicInterface = _publicInterface;
//        
//        if (!publicInterface.contains(".")) {
//            if (vlanTag == null) {
//                publicInterface += ".0";
//            } else {
//                publicInterface += "." + vlanTag;
//            }
//        }
//        
//        return publicInterface;
//    }


    /*
     * Static NAT rules
     */

//    private String genStaticNatRuleName(String publicIp, String privateIp) {
//        return genObjectName(genIpIdentifier(publicIp), genIpIdentifier(privateIp));
//    }

//    private boolean manageStaticNatRule(PaloAltoPrimative command, String publicIp, String privateIp) throws ExecutionException {
//        String ruleName = genStaticNatRuleName(publicIp, privateIp);
//        String xml;
//
//        switch (command) {
//
//        case CHECK_IF_EXISTS:
//            xml = PaloAltoXml.STATIC_NAT_RULE_GETONE.getXml();
//            xml = setDelete(xml, false);
//            xml = replaceXmlValue(xml, "rule-set", _publicZone);
//            xml = replaceXmlValue(xml, "from-zone", _publicZone);
//            xml = replaceXmlValue(xml, "rule-name", ruleName);
//            return sendRequestAndCheckResponse(command, xml, "name", ruleName);
//
//        case ADD:
//            if (manageStaticNatRule(PaloAltoPrimative.CHECK_IF_EXISTS, publicIp, privateIp)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.STATIC_NAT_RULE_ADD.getXml();
//            xml = replaceXmlValue(xml, "rule-set", _publicZone);
//            xml = replaceXmlValue(xml, "from-zone", _publicZone);
//            xml = replaceXmlValue(xml, "rule-name", ruleName);
//            xml = replaceXmlValue(xml, "original-ip", publicIp);
//            xml = replaceXmlValue(xml, "translated-ip", privateIp);
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to add static NAT rule from public IP " + publicIp + " to private IP " + privateIp);
//            } else {
//                return true;
//            }
//
//        case DELETE:
//            if (!manageStaticNatRule(PaloAltoPrimative.CHECK_IF_EXISTS, publicIp, privateIp)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.STATIC_NAT_RULE_GETONE.getXml();
//            xml = setDelete(xml, true);
//            xml = replaceXmlValue(xml, "rule-set", _publicZone);
//            xml = replaceXmlValue(xml, "from-zone", _publicZone);
//            xml = replaceXmlValue(xml, "rule-name", ruleName);
//
//            if (!sendRequestAndCheckResponse(command, xml, "name", ruleName)) {
//                throw new ExecutionException("Failed to delete static NAT rule from public IP " + publicIp + " to private IP " + privateIp);
//            } else {
//                return true;
//            }
//
//        default:
//            throw new ExecutionException("Unrecognized command.");
//
//        }
//    }
    
//    private List<String[]> getStaticNatRules(RuleMatchCondition condition, String privateGateway, Long privateCidrSize) throws ExecutionException {             
//        List<String[]> staticNatRules = new ArrayList<String[]>();
//
//        String xmlRequest = PaloAltoXml.STATIC_NAT_RULE_GETALL.getXml();
//        String xmlResponse = sendRequest(xmlRequest);       
//        Document doc = getDocument(xmlResponse);
//        NodeList rules = doc.getElementsByTagName("rule");
//        for (int i = 0; i < rules.getLength(); i++) {
//            NodeList ruleEntries = rules.item(i).getChildNodes();               
//            for (int j = 0; j < ruleEntries.getLength(); j++) {
//                Node ruleEntry = ruleEntries.item(j);
//                if (ruleEntry.getNodeName().equals("name")) {
//                    String name = ruleEntry.getFirstChild().getNodeValue();
//                    String[] nameContents = name.split("-");
//
//                    if (nameContents.length != 8) {
//                        continue;
//                    }
//
//                    String rulePublicIp = nameContents[0] + "." + nameContents[1] + "." + nameContents[2] + "." + nameContents[3];
//                    String rulePrivateIp = nameContents[4] + "." + nameContents[5] + "." + nameContents[6] + "." + nameContents[7];
//
//                    boolean addToList = false;
//                    if (condition.equals(RuleMatchCondition.ALL)) {
//                        addToList = true;
//                    } else if (condition.equals(RuleMatchCondition.PRIVATE_SUBNET)) {
//                        assert (privateGateway != null && privateCidrSize != null);
//                        addToList = NetUtils.sameSubnetCIDR(rulePrivateIp, privateGateway, privateCidrSize);
//                    } else {
//                        s_logger.error("Invalid rule match condition.");
//                        assert false;
//                    }
//
//                    if (addToList) {
//                        staticNatRules.add(new String[]{rulePublicIp, rulePrivateIp});
//                    }
//                }
//            }               
//        }
//
//        return staticNatRules;
//    }

    /*
     * Destination NAT pools
     */

//    private String genDestinationNatPoolName(String privateIp, long destPort) {
//        return genObjectName(genIpIdentifier(privateIp), String.valueOf(destPort));
//    }

//    private boolean manageDestinationNatPool(PaloAltoPrimative command, String privateIp, long destPort) throws ExecutionException {
//        String poolName = genDestinationNatPoolName(privateIp, destPort);
//        String xml;
//
//        switch (command) {
//
//        case CHECK_IF_EXISTS:
//            xml = PaloAltoXml.DEST_NAT_POOL_GETONE.getXml();
//            xml  = setDelete(xml, false);
//            xml = replaceXmlValue(xml, "pool-name", poolName);
//            return sendRequestAndCheckResponse(command, xml, "name", poolName);
//
//        case CHECK_IF_IN_USE:
//            // Check if any destination nat rules refer to this pool
//            xml = PaloAltoXml.DEST_NAT_RULE_GETALL.getXml();
//            xml = replaceXmlValue(xml, "rule-set", _publicZone);
//            return sendRequestAndCheckResponse(command, xml, "pool-name", poolName);
//
//        case ADD:
//            if (manageDestinationNatPool(PaloAltoPrimative.CHECK_IF_EXISTS, privateIp, destPort)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.DEST_NAT_POOL_ADD.getXml();
//            xml = replaceXmlValue(xml, "pool-name", poolName);
//            xml = replaceXmlValue(xml, "private-address", privateIp + "/32");
//            xml = replaceXmlValue(xml, "dest-port", String.valueOf(destPort));
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to add destination NAT pool for private IP " + privateIp + " and private port " + destPort);
//            } else {
//                return true;
//            }
//
//        case DELETE:
//            if (!manageDestinationNatPool(PaloAltoPrimative.CHECK_IF_EXISTS, privateIp, destPort)) {
//                return true;
//            }
//
//            if (manageDestinationNatPool(PaloAltoPrimative.CHECK_IF_IN_USE, privateIp, destPort)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.DEST_NAT_POOL_GETONE.getXml();
//            xml = setDelete(xml, true);
//            xml = replaceXmlValue(xml, "pool-name", poolName);
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to delete destination NAT pool for private IP " + privateIp + " and private port " + destPort);
//            } else {
//                return true;
//            }
//
//        default:
//            throw new ExecutionException("Unrecognized command.");
//        }
//    }

    /*
     * Destination NAT rules
     */

//    private String genDestinationNatRuleName(String publicIp, String privateIp, long srcPort, long destPort) {
//        return "destnatrule-" + String.valueOf(genObjectName(publicIp, privateIp, String.valueOf(srcPort), String.valueOf(destPort)).hashCode()).replaceAll("[^a-zA-Z0-9]", "");
//    }

//    private boolean manageDestinationNatRule(PaloAltoPrimative command, String publicIp, String privateIp, long srcPort, long destPort) throws ExecutionException {
//        String ruleName = genDestinationNatRuleName(publicIp, privateIp, srcPort, destPort);
//        String poolName = genDestinationNatPoolName(privateIp, destPort);
//        String xml;
//
//        switch (command) {
//
//        case CHECK_IF_EXISTS:
//            xml = PaloAltoXml.DEST_NAT_RULE_GETONE.getXml();
//            xml = setDelete(xml, false);
//            xml = replaceXmlValue(xml, "rule-set", _publicZone);
//            xml = replaceXmlValue(xml, "from-zone", _publicZone);
//            xml = replaceXmlValue(xml, "rule-name", ruleName);
//            return sendRequestAndCheckResponse(command, xml, "name", ruleName);
//
//        case ADD:
//            if (manageDestinationNatRule(PaloAltoPrimative.CHECK_IF_EXISTS, publicIp, privateIp, srcPort, destPort)) {
//                return true;
//            }
//
//            if (!manageDestinationNatPool(PaloAltoPrimative.CHECK_IF_EXISTS, privateIp, destPort)) {
//                throw new ExecutionException("The destination NAT pool corresponding to private IP: " + privateIp + " and destination port: " + destPort + " does not exist.");
//            }
//
//            xml = PaloAltoXml.DEST_NAT_RULE_ADD.getXml();
//            xml = replaceXmlValue(xml, "rule-set", _publicZone);
//            xml = replaceXmlValue(xml, "from-zone", _publicZone);
//            xml = replaceXmlValue(xml, "rule-name", ruleName);
//            xml = replaceXmlValue(xml, "public-address", publicIp);
//            xml = replaceXmlValue(xml, "src-port", String.valueOf(srcPort));
//            xml = replaceXmlValue(xml, "pool-name", poolName);
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to add destination NAT rule from public IP " + publicIp + ", public port " + srcPort + ", private IP " + privateIp + ", and private port " + destPort);
//            } else {
//                return true;
//            }
//
//        case DELETE:
//            if (!manageDestinationNatRule(PaloAltoPrimative.CHECK_IF_EXISTS, publicIp, privateIp, srcPort, destPort)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.DEST_NAT_RULE_GETONE.getXml();
//            xml = setDelete(xml, true);
//            xml = replaceXmlValue(xml, "rule-set", _publicZone);
//            xml = replaceXmlValue(xml, "from-zone", _publicZone);
//            xml = replaceXmlValue(xml, "rule-name", ruleName);
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to delete destination NAT rule from public IP " + publicIp + ", public port " + srcPort + ", private IP " + privateIp + ", and private port " + destPort);
//            } else {
//                return true;
//            }
//
//        default:
//            s_logger.debug("Unrecognized command.");
//            return false;
//        }
//
//    }
    
//    private List<String[]> getDestNatRules(RuleMatchCondition condition, String publicIp, String privateIp, String privateGateway, Long privateCidrSize) throws ExecutionException {
//        List<String[]> destNatRules = new ArrayList<String[]>();
//
//        String xmlRequest = PaloAltoXml.DEST_NAT_RULE_GETALL.getXml();
//        xmlRequest = replaceXmlValue(xmlRequest, "rule-set", _publicZone);
//        String xmlResponse = sendRequest(xmlRequest);
//        Document doc = getDocument(xmlResponse);
//        NodeList rules = doc.getElementsByTagName("rule");
//        for (int ruleIndex = 0; ruleIndex < rules.getLength(); ruleIndex++) {
//            String rulePublicIp = null;
//            String rulePrivateIp = null;
//            String ruleSrcPort = null;
//            String ruleDestPort = null;
//            NodeList ruleEntries = rules.item(ruleIndex).getChildNodes();
//            for (int ruleEntryIndex = 0; ruleEntryIndex < ruleEntries.getLength(); ruleEntryIndex++) {
//                Node ruleEntry = ruleEntries.item(ruleEntryIndex);
//                if (ruleEntry.getNodeName().equals("dest-nat-rule-match")) {
//                    NodeList ruleMatchEntries = ruleEntry.getChildNodes();
//                    for (int ruleMatchIndex = 0; ruleMatchIndex < ruleMatchEntries.getLength(); ruleMatchIndex++) {
//                        Node ruleMatchEntry = ruleMatchEntries.item(ruleMatchIndex);
//                        if (ruleMatchEntry.getNodeName().equals("destination-address")) {
//                            NodeList destAddressEntries = ruleMatchEntry.getChildNodes();
//                            for (int destAddressIndex = 0; destAddressIndex < destAddressEntries.getLength(); destAddressIndex++) {
//                                Node destAddressEntry = destAddressEntries.item(destAddressIndex);
//                                if (destAddressEntry.getNodeName().equals("dst-addr")) {
//                                    rulePublicIp = destAddressEntry.getFirstChild().getNodeValue().split("/")[0];
//                                }
//                            }
//                        } else if (ruleMatchEntry.getNodeName().equals("destination-port")) {
//                            NodeList destPortEntries = ruleMatchEntry.getChildNodes();
//                            for (int destPortIndex = 0; destPortIndex < destPortEntries.getLength(); destPortIndex++) {
//                                Node destPortEntry = destPortEntries.item(destPortIndex);
//                                if (destPortEntry.getNodeName().equals("dst-port")) {
//                                    ruleSrcPort = destPortEntry.getFirstChild().getNodeValue();
//                                }
//                            }
//                        }
//                    }
//                } else if (ruleEntry.getNodeName().equals("then")) {
//                    NodeList ruleThenEntries = ruleEntry.getChildNodes();
//                    for (int ruleThenIndex = 0; ruleThenIndex < ruleThenEntries.getLength(); ruleThenIndex++) {
//                        Node ruleThenEntry = ruleThenEntries.item(ruleThenIndex);
//                        if (ruleThenEntry.getNodeName().equals("destination-nat")) {
//                            NodeList destNatEntries = ruleThenEntry.getChildNodes();
//                            for (int destNatIndex = 0; destNatIndex < destNatEntries.getLength(); destNatIndex++) {
//                                Node destNatEntry = destNatEntries.item(destNatIndex);
//                                if (destNatEntry.getNodeName().equals("pool")) {
//                                    NodeList poolEntries = destNatEntry.getChildNodes();
//                                    for (int poolIndex = 0; poolIndex < poolEntries.getLength(); poolIndex++) {
//                                        Node poolEntry = poolEntries.item(poolIndex);
//                                        if (poolEntry.getNodeName().equals("pool-name")) {
//                                            String[] poolName = poolEntry.getFirstChild().getNodeValue().split("-");
//                                            if (poolName.length == 5) {
//                                                rulePrivateIp = poolName[0] + "." + poolName[1] + "." + poolName[2] + "." + poolName[3];
//                                                ruleDestPort = poolName[4];
//                                            }
//                                        }
//                                    }
//                                }
//                            }
//                        }
//                    }
//                }
//            }
//
//            if (rulePublicIp == null || rulePrivateIp == null || ruleSrcPort == null || ruleDestPort == null) {
//                continue;
//            }
//
//            boolean addToList = false;
//            if (condition.equals(RuleMatchCondition.ALL)) {
//                addToList = true;
//            } else if (condition.equals(RuleMatchCondition.PUBLIC_PRIVATE_IPS)) {
//                assert (publicIp != null && privateIp != null);
//                addToList = publicIp.equals(rulePublicIp) && privateIp.equals(rulePrivateIp);
//            } else if (condition.equals(RuleMatchCondition.PRIVATE_SUBNET)) {
//                assert (privateGateway != null && privateCidrSize != null);
//                addToList = NetUtils.sameSubnetCIDR(rulePrivateIp, privateGateway, privateCidrSize);
//            }
//
//            if (addToList) {
//                destNatRules.add(new String[]{rulePublicIp, rulePrivateIp, ruleSrcPort, ruleDestPort});
//            }
//        }
//
//        return destNatRules;
//    }        

    /*
     * Source NAT pools
     */

//    private String genSourceNatPoolName(String publicIp) {
//        return genObjectName(genIpIdentifier(publicIp));
//    }

    /*
     * Source NAT rules
     */

    private String genSourceNatRuleName(Long privateVlanTag) {
        return "src_nat."+Long.toString(privateVlanTag);
    }

    public boolean manageNatRule(ArrayList<IPaloAltoCommand> cmdList, PaloAltoPrimative prim, GuestNetworkType type, Long publicVlanTag, String publicIp, long privateVlanTag, String privateGateway) throws ExecutionException {
        String _public_entry_name = genPublicInterfaceName(publicIp);
        String _private_entry_name = genPrivateInterfaceName(privateVlanTag);
        String _src_nat_entry_name = genSourceNatRuleName(privateVlanTag);

        switch (prim) {

        case CHECK_IF_EXISTS:
            // check if one exists already
            Map<String, String> params = new HashMap<String, String>();
            params.put("type", "config");
            params.put("action", "get");
            params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/rulebase/nat/rules/entry[@name='"+_src_nat_entry_name+"']");
            String response = request(PaloAltoMethod.GET, params);
            boolean result = (validResponse(response) && responseNotEmpty(response));
            s_logger.debug("Source NAT exists: "+_src_nat_entry_name+", "+result);
            return result;

        case ADD:
            if (manageNatRule(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS, type, publicVlanTag, publicIp, privateVlanTag, privateGateway)) {
                return true;
            }

            // add cmds
            // add source nat
            String xml = PaloAltoXml.SOURCE_NAT_ADD.getXml();                              
            xml = replaceXmlValue(xml, "from", _privateZone);
            xml = replaceXmlValue(xml, "to", _publicZone);
            xml = replaceXmlValue(xml, "source", privateGateway);
            xml = replaceXmlValue(xml, "destination", publicIp);
            xml = replaceXmlValue(xml, "to_interface", _public_entry_name);
            xml = replaceXmlValue(xml, "vlan", Long.toString(privateVlanTag));

            Map<String, String> a_params = new HashMap<String, String>();
            a_params.put("type", "config");
            a_params.put("action", "set");
            a_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/rulebase/nat/rules/entry[@name='"+_src_nat_entry_name+"']");
            a_params.put("element", xml);
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.POST, a_params));

            return true;

        case DELETE:
            if (!manageNatRule(cmdList, PaloAltoPrimative.CHECK_IF_EXISTS, type, publicVlanTag, publicIp, privateVlanTag, privateGateway)) {
                return true;
            }

            // add cmds to the list
            // remove source nat rule
            Map<String, String> d_params = new HashMap<String, String>();
            d_params.put("type", "config");
            d_params.put("action", "delete");
            d_params.put("xpath", "/config/devices/entry/vsys/entry[@name='vsys1']/rulebase/nat/rules/entry[@name='"+_src_nat_entry_name+"']");
            cmdList.add(new DefaultPaloAltoCommand(PaloAltoMethod.POST, d_params));

            return true;

        default:
            s_logger.debug("Unrecognized command.");
            return false;
        }
    }


    /*
     * Address book entries
     */

//    private String genAddressBookEntryName(String ip) {
//        if (ip == null) {
//            return "any";
//        } else {
//            return genIpIdentifier(ip);
//        }
//    }

//    private boolean manageAddressBookEntry(PaloAltoPrimative command, String zone, String ip, String entryName) throws ExecutionException {
//        if (!zone.equals(_publicZone) && !zone.equals(_privateZone)) {
//            throw new ExecutionException("Invalid zone.");
//        }
//
//        if (entryName == null) {
//            entryName = genAddressBookEntryName(ip);
//        }
//
//        String xml;
//
//        switch (command) {
//
//        case CHECK_IF_EXISTS:
//            xml = PaloAltoXml.ADDRESS_BOOK_ENTRY_GETONE.getXml();
//            xml = setDelete(xml, false);
//            xml = replaceXmlValue(xml, "zone", zone);
//            xml = replaceXmlValue(xml, "entry-name", entryName);
//            return sendRequestAndCheckResponse(command, xml, "name", entryName);
//
//        case CHECK_IF_IN_USE:
//            // Check if any security policies refer to this address book entry
//            xml = PaloAltoXml.SECURITY_POLICY_GETALL.getXml();
//            String fromZone = zone.equals(_publicZone) ? _privateZone : _publicZone;
//            xml = replaceXmlValue(xml, "from-zone", fromZone);
//            xml = replaceXmlValue(xml, "to-zone", zone);
//            return sendRequestAndCheckResponse(command, xml, "destination-address", entryName);
//
//        case ADD:
//            if (manageAddressBookEntry(PaloAltoPrimative.CHECK_IF_EXISTS, zone, ip, entryName)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.ADDRESS_BOOK_ENTRY_ADD.getXml();
//            xml = replaceXmlValue(xml, "zone", zone);
//            xml = replaceXmlValue(xml, "entry-name", entryName);
//            xml = replaceXmlValue(xml, "ip", ip);
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to add address book entry for IP " + ip + " in zone " + zone);
//            } else {
//                return true;
//            }
//
//        case DELETE:
//            if (!manageAddressBookEntry(PaloAltoPrimative.CHECK_IF_EXISTS, zone, ip, entryName)) {
//                return true;
//            }
//
//            if (manageAddressBookEntry(PaloAltoPrimative.CHECK_IF_IN_USE, zone, ip, entryName)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.ADDRESS_BOOK_ENTRY_GETONE.getXml();
//            xml = setDelete(xml, true);
//            xml = replaceXmlValue(xml, "zone", zone);
//            xml = replaceXmlValue(xml, "entry-name", entryName);
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to delete address book entry for IP " + ip + " in zone " + zone);
//            } else {
//                return true;
//            }
//
//        default:
//            s_logger.debug("Unrecognized command.");
//            return false;
//
//        }
//
//    }

    /*
     * Applications
     */

//    private String genApplicationName(Protocol protocol, int startPort, int endPort) {
//        if (protocol.equals(Protocol.any)) {
//            return Protocol.any.toString();
//        } else {
//            return genObjectName(protocol.toString(), String.valueOf(startPort), String.valueOf(endPort));
//        }
//    }

//    private Object[] parseApplicationName(String applicationName) throws ExecutionException {
//        String errorMsg = "Invalid application: " + applicationName;
//        String[] applicationComponents = applicationName.split("-");
//
//        Protocol protocol;
//        Integer startPort;
//        Integer endPort;
//        try {
//            protocol = getProtocol(applicationComponents[0]);           
//            startPort = Integer.parseInt(applicationComponents[1]);
//            endPort = Integer.parseInt(applicationComponents[2]);
//        } catch (Exception e) {
//            throw new ExecutionException(errorMsg);
//        }
//
//        return new Object[]{protocol, startPort, endPort};
//    }

//    private boolean manageApplication(PaloAltoPrimative command, Protocol protocol, int startPort, int endPort) throws ExecutionException {
//        if (protocol.equals(Protocol.any)) {
//            return true;
//        }
//
//        String applicationName = genApplicationName(protocol, startPort, endPort);
//        String xml;
//
//        switch (command) {
//
//        case CHECK_IF_EXISTS:
//            xml = PaloAltoXml.APPLICATION_GETONE.getXml();
//            xml = setDelete(xml, false);
//            xml = replaceXmlValue(xml, "name", applicationName);
//            return sendRequestAndCheckResponse(command, xml, "name", applicationName);
//
//        case ADD:
//            if (manageApplication(PaloAltoPrimative.CHECK_IF_EXISTS, protocol, startPort, endPort)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.APPLICATION_ADD.getXml();
//            xml = replaceXmlValue(xml, "name", applicationName);
//            xml = replaceXmlValue(xml, "protocol", protocol.toString());
//
//            String destPort;
//            if (startPort == endPort) {
//                destPort = String.valueOf(startPort);
//            } else {
//                destPort = startPort + "-" + endPort;
//            }
//
//            xml = replaceXmlValue(xml, "dest-port", destPort);
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to add application " + applicationName);
//            } else {
//                return true;
//            }
//
//        case DELETE:
//            if (!manageApplication(PaloAltoPrimative.CHECK_IF_EXISTS, protocol, startPort, endPort)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.APPLICATION_GETONE.getXml();
//            xml = setDelete(xml, true);
//            xml = replaceXmlValue(xml, "name", applicationName);
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to delete application " + applicationName);
//            } else {
//                return true;
//            }
//
//        default:
//            s_logger.debug("Unrecognized command.");
//            return false;
//        }
//
//    }

//    private List<String> getUnusedApplications(List<String> applications) throws ExecutionException {
//        List<String> unusedApplications = new ArrayList<String>();
//
//        // Check if any of the applications are unused by existing security policies
//        String xml = PaloAltoXml.SECURITY_POLICY_GETALL.getXml();
//        xml = replaceXmlValue(xml, "from-zone", _publicZone);
//        xml = replaceXmlValue(xml, "to-zone", _privateZone);
//        String allPolicies = sendRequest(xml);
//
//        for (String application : applications) {
//            if (!application.equals(Protocol.any.toString()) && !allPolicies.contains(application)) {
//                unusedApplications.add(application);
//            }
//        }
//
//        return unusedApplications;
//    }
    
//    private List<String> getApplicationsForSecurityPolicy(SecurityPolicyType type, String privateIp) throws ExecutionException {
//        String fromZone = _publicZone;
//        String toZone = _privateZone;
//        String policyName = genSecurityPolicyName(type, null, null, fromZone, toZone, privateIp);
//        String xml = PaloAltoXml.SECURITY_POLICY_GETONE.getXml();
//        xml = setDelete(xml, false);
//        xml = replaceXmlValue(xml, "from-zone", fromZone);
//        xml = replaceXmlValue(xml, "to-zone", toZone);
//        xml = replaceXmlValue(xml, "policy-name", policyName);
//        String policy = sendRequest(xml);
//
//        Document doc = getDocument(policy);
//
//        List<String> policyApplications = new ArrayList<String>();
//        NodeList applicationNodes = doc.getElementsByTagName("application");
//
//        for (int i = 0; i < applicationNodes.getLength(); i++) {
//            Node applicationNode = applicationNodes.item(i);
//            policyApplications.add(applicationNode.getFirstChild().getNodeValue());
//        }               
//
//        return policyApplications;
//    }       

//    private List<Object[]> extractApplications(List<FirewallRuleTO> rules) throws ExecutionException {
//        List<Object[]> applications = new ArrayList<Object[]>();
//
//        for (FirewallRuleTO rule : rules) {
//            Object[] application = new Object[3];
//            application[0] = getProtocol(rule.getProtocol());
//            application[1] = rule.getSrcPortRange()[0];
//            application[2] = rule.getSrcPortRange()[1];
//            applications.add(application);
//        }
//
//        return applications;
//    }
    
    /*
     * Security policies
     */

//    private String genSecurityPolicyName(SecurityPolicyType type, Long accountId, String username, String fromZone, String toZone, String translatedIp) {
//        if (type.equals(SecurityPolicyType.VPN)) {
//            return genObjectName(_vpnObjectPrefix, String.valueOf(accountId), username);
//        } else {
//            return genObjectName(type.getIdentifier(), fromZone, toZone, genIpIdentifier(translatedIp));
//        }               
//    }

//    private boolean manageSecurityPolicy(SecurityPolicyType type, PaloAltoPrimative command, Long accountId, String username, String privateIp, List<String> applicationNames, String ipsecVpnName) throws ExecutionException {
//        String fromZone = _publicZone;
//        String toZone = _privateZone;
//        
//        String securityPolicyName;
//        String addressBookEntryName;
//        
//        if (type.equals(SecurityPolicyType.VPN) && ipsecVpnName != null) {
//            securityPolicyName = ipsecVpnName;
//            addressBookEntryName = ipsecVpnName;
//        } else {
//            securityPolicyName = genSecurityPolicyName(type, accountId, username, fromZone, toZone, privateIp);
//            addressBookEntryName = genAddressBookEntryName(privateIp);
//        }        
//
//        String xml;
//
//        switch (command) {
//
//        case CHECK_IF_EXISTS:
//            xml = PaloAltoXml.SECURITY_POLICY_GETONE.getXml();
//            xml = setDelete(xml, false);
//            xml = replaceXmlValue(xml, "from-zone", fromZone);
//            xml = replaceXmlValue(xml, "to-zone", toZone);
//            xml = replaceXmlValue(xml, "policy-name", securityPolicyName);
//            
//            return sendRequestAndCheckResponse(command, xml, "name", securityPolicyName);
//
//        case CHECK_IF_IN_USE:
//            List<String[]> rulesToCheck = null; 
//            if (type.equals(SecurityPolicyType.STATIC_NAT)) {
//                // Check if any static NAT rules rely on this security policy
//                //rulesToCheck = getStaticNatRules(RuleMatchCondition.ALL, null, null);
//            } else if (type.equals(SecurityPolicyType.DESTINATION_NAT)) {
//                // Check if any destination NAT rules rely on this security policy
//                //rulesToCheck = getDestNatRules(RuleMatchCondition.ALL, null, null, null, null);
//            } else {
//                return false;
//            }                   
//
//            for (String[] rule : rulesToCheck) {
//                String rulePrivateIp = rule[1];
//                if (privateIp.equals(rulePrivateIp)) {
//                    return true;
//                }
//            }
//
//            return false;
//
//        case ADD:
//            if (!manageAddressBookEntry(PaloAltoPrimative.CHECK_IF_EXISTS, toZone, privateIp, ipsecVpnName)) {
//                throw new ExecutionException("No address book entry for policy: " + securityPolicyName);
//            }
//
//            xml = PaloAltoXml.SECURITY_POLICY_ADD.getXml();                              
//            xml = replaceXmlValue(xml, "from-zone", fromZone);
//            xml = replaceXmlValue(xml, "to-zone", toZone);            
//            xml = replaceXmlValue(xml, "policy-name", securityPolicyName);            
//            xml = replaceXmlValue(xml, "src-address", "any");    
//            xml = replaceXmlValue(xml, "dest-address", addressBookEntryName);
//            
//            if (type.equals(SecurityPolicyType.VPN) && ipsecVpnName != null) {
//                xml = replaceXmlValue(xml, "tunnel", "<tunnel><ipsec-vpn>" + ipsecVpnName + "</ipsec-vpn></tunnel>");
//            } else {        
//                xml = replaceXmlValue(xml, "tunnel", "");
//            }
//                        
//            String applications;
//            if (applicationNames == null) {
//                applications = "<application>any</application>";
//            } else {
//                applications = "";
//                for (String applicationName : applicationNames) {
//                    applications += "<application>" + applicationName + "</application>";
//                }
//            }           
//
//            xml = replaceXmlValue(xml, "applications", applications);
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to add security policy for privateIp " + privateIp + " and applications " + applicationNames);
//            } else {
//                return true;
//            }
//
//        case DELETE:
//            if (!manageSecurityPolicy(type, PaloAltoPrimative.CHECK_IF_EXISTS, null, null, privateIp, applicationNames, ipsecVpnName)) {
//                return true;
//            }
//
//            if (manageSecurityPolicy(type, PaloAltoPrimative.CHECK_IF_IN_USE, null, null, privateIp, applicationNames, ipsecVpnName)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.SECURITY_POLICY_GETONE.getXml();
//            xml = setDelete(xml, true);
//            xml = replaceXmlValue(xml, "from-zone", fromZone);
//            xml = replaceXmlValue(xml, "to-zone", toZone);
//            xml = replaceXmlValue(xml, "policy-name", securityPolicyName);
//            
//            boolean success = sendRequestAndCheckResponse(command, xml);
//
//            if (success) {
//                xml = PaloAltoXml.SECURITY_POLICY_GETALL.getXml();
//                xml = replaceXmlValue(xml, "from-zone", fromZone);
//                xml = replaceXmlValue(xml, "to-zone", toZone);
//                String getAllResponseXml = sendRequest(xml);
//
//                if (getAllResponseXml == null) {
//                    throw new ExecutionException("Deleted security policy, but failed to delete security policy group.");
//                } 
//                
//                if (!getAllResponseXml.contains(fromZone) || !getAllResponseXml.contains(toZone)) {
//                    return true;
//                } else if (!getAllResponseXml.contains("match") && !getAllResponseXml.contains("then")) {
//                    xml = PaloAltoXml.SECURITY_POLICY_GROUP.getXml();
//                    xml = replaceXmlValue(xml, "from-zone", fromZone);
//                    xml = replaceXmlValue(xml, "to-zone", toZone);
//                    xml = setDelete(xml, true);
//                    if (!sendRequestAndCheckResponse(command, xml)) {
//                        throw new ExecutionException("Deleted security policy, but failed to delete security policy group.");
//                    } else {
//                        return true;
//                    }
//                } else {
//                    return true;
//                }
//            } else {
//                throw new ExecutionException("Failed to delete security policy for privateIp " + privateIp + " and applications " + applicationNames);
//            }
//
//        default:
//            s_logger.debug("Unrecognized command.");
//            return false;
//
//        }
//    }   
    
//    private boolean addSecurityPolicyAndApplications(SecurityPolicyType type, String privateIp, List<Object[]> applications) throws ExecutionException {
//        // Add all necessary applications
//        List<String> applicationNames = new ArrayList<String>();
//        for (Object[] application : applications) {         
//            Protocol protocol = (Protocol) application[0];
//            int startPort = application[1] != null ? ((Integer) application[1]) : -1;
//            int endPort = application[2] != null ? ((Integer) application[2]) : -1;
//
//            String applicationName = genApplicationName(protocol, startPort, endPort);
//            if (!applicationNames.contains(applicationName)) {
//                applicationNames.add(applicationName);
//            }
//
//            //manageApplication(PaloAltoPrimative.ADD, protocol, startPort, endPort);
//        }
//
//        // Add a new security policy
//        //manageSecurityPolicy(type, PaloAltoPrimative.ADD, null, null, privateIp, applicationNames, null);
//
//        return true;
//    }

//    private boolean removeSecurityPolicyAndApplications(SecurityPolicyType type, String privateIp) throws ExecutionException {
//        if (!manageSecurityPolicy(type, PaloAltoPrimative.CHECK_IF_EXISTS, null, null, privateIp, null, null)) {
//            return true;
//        }
//
//        if (manageSecurityPolicy(type, PaloAltoPrimative.CHECK_IF_IN_USE, null, null, privateIp, null, null)) {
//            return true;
//        }
//
//        // Get a list of applications for this security policy
//        List<String> applications = getApplicationsForSecurityPolicy(type, privateIp);
//
//        // Remove the security policy 
//        manageSecurityPolicy(type, PaloAltoPrimative.DELETE, null, null, privateIp, null, null);
//
//        // Remove any applications for the removed security policy that are no longer in use
//        //List<String> unusedApplications = getUnusedApplications(applications);
//        for (String application : unusedApplications) {
//            Object[] applicationComponents;
//
//            try {
//                applicationComponents = parseApplicationName(application);
//            } catch (ExecutionException e) {
//                s_logger.error("Found an invalid application: " + application + ". Not attempting to clean up.");
//                continue;
//            }
//
//            Protocol protocol = (Protocol) applicationComponents[0];
//            Integer startPort = (Integer) applicationComponents[1];
//            Integer endPort = (Integer) applicationComponents[2];           
//            //manageApplication(PaloAltoPrimative.DELETE, protocol, startPort, endPort); 
//        }
//
//        return true;
//    }

    /*
     * Filter terms
     */

//    private String genIpFilterTermName(String ipAddress) {
//        return genIpIdentifier(ipAddress);
//    }

//    private boolean manageUsageFilter(PaloAltoPrimative command, UsageFilter filter, String ip, Long guestVlanTag, String filterTermName) throws ExecutionException {              
//        String filterName;
//        String filterDescription;
//        String xml;
//
//        if (filter.equals(_usageFilterIPInput) || filter.equals(_usageFilterIPOutput)) {
//            assert (ip != null && guestVlanTag == null);            
//            filterName = filter.getName();
//            filterDescription = filter.toString() + ", public IP = " + ip;
//            xml = PaloAltoXml.PUBLIC_IP_FILTER_TERM_ADD.getXml();
//        } else if (filter.equals(_usageFilterVlanInput) || filter.equals(_usageFilterVlanOutput)) {
//            assert (ip == null && guestVlanTag != null);            
//            filterName = filter.getName() + "-" + guestVlanTag;      
//            filterDescription = filter.toString() + ", guest VLAN tag = " + guestVlanTag;
//            filterTermName = filterName;
//            xml = PaloAltoXml.GUEST_VLAN_FILTER_TERM_ADD.getXml();
//        } else {
//            return false;
//        }
//
//        switch(command) {
//
//        case CHECK_IF_EXISTS:
//            xml = PaloAltoXml.FILTER_TERM_GETONE.getXml();
//            xml = setDelete(xml, false);
//            xml = replaceXmlValue(xml, "filter-name", filterName);
//            xml = replaceXmlValue(xml, "term-name", filterTermName);
//            return sendRequestAndCheckResponse(command, xml, "name", filterTermName);
//
//        case ADD:   
//            if (manageUsageFilter(PaloAltoPrimative.CHECK_IF_EXISTS, filter, ip, guestVlanTag, filterTermName)) {
//                return true;
//            }
//
//            xml = replaceXmlValue(xml, "filter-name", filterName);
//            xml = replaceXmlValue(xml, "term-name", filterTermName);
//
//            if (filter.equals(_usageFilterIPInput) || filter.equals(_usageFilterIPOutput)) {
//                xml = replaceXmlValue(xml, "ip-address", ip);
//                xml = replaceXmlValue(xml, "address-type", filter.getAddressType());
//            }
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to add usage filter: " + filterDescription);
//            } else {
//                return true;
//            }
//
//        case DELETE:
//            if (!manageUsageFilter(PaloAltoPrimative.CHECK_IF_EXISTS, filter, ip, guestVlanTag, filterTermName)) {
//                return true;
//            }
//
//            boolean deleteFilter = filter.equals(_usageFilterVlanInput) || filter.equals(_usageFilterVlanOutput);
//            xml = deleteFilter ? PaloAltoXml.FILTER_GETONE.getXml() : PaloAltoXml.FILTER_TERM_GETONE.getXml();
//            xml = setDelete(xml, true);
//            xml = replaceXmlValue(xml, "filter-name", filterName);
//            xml = !deleteFilter ? replaceXmlValue(xml, "term-name", filterTermName) : xml;
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to delete usage filter: " + filterDescription);
//            } else {
//                return true;
//            }
//
//        default:
//            s_logger.debug("Unrecognized command.");
//            return false;
//
//        }
//    }   

//    private String genNameValueEntry(String name, String value) {
//        String xml = PaloAltoXml.TEMPLATE_ENTRY.getXml();
//        xml = replaceXmlValue(xml, "name", name);
//        xml = replaceXmlValue(xml, "value", value);
//        return xml;
//    }
//    
//    private String genMultipleEntries(String name, List<String> values) {
//        String result = "";
//        for (String value : values) {
//            result = result + genNameValueEntry(name, value);
//        }
//        return result;
//    }
//    
//    private String genPortRangeEntry(String protocol, String portRange) {
//        String result = "";
//        result = result + genNameValueEntry("protocol", protocol);
//        result = result + genNameValueEntry("destination-port", portRange);
//        return result;
//    }
//    
//    private String genIcmpEntries(String icmpType, String icmpCode) {
//        String result = "";
//        result = result + genNameValueEntry("protocol", "icmp");
//        if (icmpType.equals("-1")) {
//            result = result + genNameValueEntry("icmp-type", "0-255");
//        } else {
//            result = result + genNameValueEntry("icmp-type", icmpType);
//        }
//        if (icmpCode.equals("-1")) {
//            result = result + genNameValueEntry("icmp-code", "0-255");
//        } else {
//            result = result + genNameValueEntry("icmp-code", icmpCode);
//        }
//        return result;
//    }
    
//    private boolean manageFirewallFilter(PaloAltoPrimative command, FirewallFilterTerm term, String filterName) throws ExecutionException {                
//        String xml;
//
//        switch(command) {
//
//        case CHECK_IF_EXISTS:
//            xml = PaloAltoXml.FIREWALL_FILTER_TERM_GETONE.getXml();
//            xml = setDelete(xml, false);
//            xml = replaceXmlValue(xml, "filter-name", filterName);
//            xml = replaceXmlValue(xml, "term-name", term.getName());
//            return sendRequestAndCheckResponse(command, xml, "name", term.getName());
//
//        case ADD:   
//            if (manageFirewallFilter(PaloAltoPrimative.CHECK_IF_EXISTS, term, filterName)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.FIREWALL_FILTER_TERM_ADD.getXml();
//            
//            xml = replaceXmlValue(xml, "filter-name", filterName);
//            xml = replaceXmlValue(xml, "term-name", term.getName());
//            xml = replaceXmlValue(xml, "source-address-entries", genMultipleEntries("source-address", term.getSourceCidrs()));
//            xml = replaceXmlValue(xml, "dest-ip-address", term.getDestIp());
//            
//            String protocol = term.getProtocol();
//            if (protocol.equals("tcp") || protocol.equals("udp")) {
//                xml = replaceXmlValue(xml, "protocol-options", genPortRangeEntry(protocol, term.getPortRange()));
//            } else if (protocol.equals("icmp")) {
//                xml = replaceXmlValue(xml, "protocol-options", genIcmpEntries(term.getIcmpType(), term.getIcmpCode()));
//            } else {
//                assert protocol.equals("any");
//                xml = replaceXmlValue(xml, "protocol-options", "");
//            }
//            xml = replaceXmlValue(xml, "count-name", term.getCountName());
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to add firewall filter: " + term.getName());
//            } else {
//                return true;
//            }
//
//        case DELETE:
//            if (!manageFirewallFilter(PaloAltoPrimative.CHECK_IF_EXISTS, term, filterName)) {
//                return true;
//            }
//
//            xml = PaloAltoXml.FIREWALL_FILTER_TERM_GETONE.getXml();
//            xml = setDelete(xml, true);
//            xml = replaceXmlValue(xml, "filter-name", filterName);
//            xml = replaceXmlValue(xml, "term-name", term.getName());
//
//            if (!sendRequestAndCheckResponse(command, xml)) {
//                throw new ExecutionException("Failed to delete firewall filter: " + term.getName());
//            } else {
//                return true;
//            }
//
//        default:
//            s_logger.debug("Unrecognized command.");
//            return false;
//
//        }
//    }   

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






//    private String sendRequestPrim(PrintWriter sendStream, BufferedReader recvStream, String xmlRequest) throws ExecutionException {
//        if (!xmlRequest.contains("request-login")) {
//            s_logger.debug("Sending request: " + xmlRequest);
//        } else {
//            s_logger.debug("Sending login request");
//        }
//                
//        boolean timedOut = false;
//        StringBuffer xmlResponseBuffer = new StringBuffer("");
//        try {
//            sendStream.write(xmlRequest);
//            sendStream.flush();
//
//            String line = "";           
//            while ((line = recvStream.readLine()) != null) {
//                xmlResponseBuffer.append(line);
//                if (line.contains("</rpc-reply>")) {
//                    break;
//                }
//            }
//
//        } catch (SocketTimeoutException e) {
//            s_logger.debug(e);
//            timedOut = true;
//        } catch (IOException e) {
//            s_logger.debug(e);
//            return null;
//        }
//
//        String xmlResponse = xmlResponseBuffer.toString();
//        String errorMsg = null;
//
//        if (timedOut) {
//            errorMsg = "Timed out on XML request: " + xmlRequest;
//        } else if (xmlResponse.isEmpty()) {
//            errorMsg = "Received an empty XML response.";
//        } else if (xmlResponse.contains("Unexpected XML tag type")) {
//            errorMsg = "Sent a command without being logged in.";
//        } else if (!xmlResponse.contains("</rpc-reply>")) {
//            errorMsg = "Didn't find the rpc-reply tag in the XML response.";
//        }
//        
//        if (errorMsg == null) {
//            return xmlResponse;
//        } else {
//            s_logger.error(errorMsg);
//            throw new ExecutionException(errorMsg);
//        }
//    }
//    
//    private String sendRequest(String xmlRequest) throws ExecutionException {
//        return sendRequestPrim(_toPaloAlto, _fromPaloAlto, xmlRequest);
//    }
//    
//    private String sendUsageRequest(String xmlRequest) throws ExecutionException {
//        return sendRequestPrim(_UsagetoPaloAlto, _UsagefromPaloAlto, xmlRequest);
//    }
//
//    private boolean checkResponse(String xmlResponse, boolean errorKeyAndValue, String key, String value) {
//        if (xmlResponse == null) {
//            s_logger.error("Failed to communicate with Palo Alto!");
//            return false;
//        }
//
//        if (!xmlResponse.contains("authentication-response")) {
//            s_logger.debug("Checking response: " + xmlResponse);
//        } else {
//            s_logger.debug("Checking login response");
//        }
//
//        String textToSearchFor = key;
//        if (value != null) {
//            textToSearchFor = "<" + key + ">" + value + "</" + key + ">";
//        }
//
//        if ((errorKeyAndValue && !xmlResponse.contains(textToSearchFor)) ||
//                (!errorKeyAndValue && xmlResponse.contains(textToSearchFor))) {
//            return true;
//        }
//
//
//        String responseMessage = extractXml(xmlResponse, "message");
//        if (responseMessage != null) {
//            s_logger.error("Request failed due to: " + responseMessage);
//        } else {
//            if (errorKeyAndValue) {
//                s_logger.error("Found error (" + textToSearchFor + ") in response.");
//            } else {
//                s_logger.debug("Didn't find " + textToSearchFor + " in response.");
//            }
//        }
//
//        return false;
//    }
//
//    private boolean sendRequestAndCheckResponse(PaloAltoPrimative command, String xmlRequest, String... keyAndValue) throws ExecutionException {
//        boolean errorKeyAndValue = false;
//        String key;
//        String value;
//
//        switch (command) {
//
//        case LOGIN:
//            key = "status";
//            value = "success";
//            break;
//
//        case OPEN_CONFIGURATION:
//        case CLOSE_CONFIGURATION:
//            errorKeyAndValue = true;
//            key = "error";
//            value = null;
//            break;
//
//        case COMMIT:
//            key = "commit-success";
//            value = null;
//            break;
//
//        case CHECK_IF_EXISTS:
//        case CHECK_IF_IN_USE:
//            assert (keyAndValue != null && keyAndValue.length == 2) : "If the PaloAltoPrimative is " + command + ", both a key and value must be specified.";
//
//            key = keyAndValue[0];
//            value = keyAndValue[1];
//            break;
//
//        default:
//            key = "load-success";
//            value = null;
//            break;
//
//        }
//
//        String xmlResponse = sendRequest(xmlRequest);
//        return checkResponse(xmlResponse, errorKeyAndValue, key, value);
//    }
//    
//    private boolean sendUsageRequestAndCheckResponse(PaloAltoPrimative command, String xmlRequest, String... keyAndValue) throws ExecutionException {                                                            
//        boolean errorKeyAndValue = false;                                                                                                                                                                 
//        String key;                                                                                                                                                                                       
//        String value;                                                                                                                                                                                     
//                                                                                                                                                                                                          
//        switch (command) {                                                                                                                                                                                
//                                                                                                                                                                                                          
//        case LOGIN:                                                                                                                                                                                       
//            key = "status";                                                                                                                                                                               
//            value = "success";                                                                                                                                                                            
//            break;                                                                                                                                                                                        
//                                                                                                                                                                                                          
//        case OPEN_CONFIGURATION:                                                                                                                                                                          
//        case CLOSE_CONFIGURATION:                                                                                                                                                                         
//            errorKeyAndValue = true;                                                                                                                                                                      
//            key = "error";                                                                                                                                                                                
//            value = null;                                                                                                                                                                                 
//            break;                                                                                                                                                                                        
//                                                                                                                                                                                                          
//        case COMMIT:                                                                                                                                                                                      
//            key = "commit-success";                                                                                                                                                                       
//            value = null;                                                                                                                                                                                 
//            break;                                                                                                                                                                                        
//                                                                                                                                                                                                          
//        case CHECK_IF_EXISTS:                                                                                                                                                                             
//        case CHECK_IF_IN_USE:                                                                                                                                                                             
//            assert (keyAndValue != null && keyAndValue.length == 2) : "If the PaloAltoPrimative is " + command + ", both a key and value must be specified.";                                                    
//                                                                                                                                                                                                          
//            key = keyAndValue[0];                                                                                                                                                                         
//            value = keyAndValue[1];                                                                                                                                                                       
//            break;                                                                                                                                                                                        
//                                                                                                                                                                                                          
//        default:                                                                                                                                                                                          
//            key = "load-success";                                                                                                                                                                         
//            value = null;                                                                                                                                                                                 
//            break;                                                                                                                                                                                        
//                                                                                                                                                                                                          
//        }                                                                                                                                                                                                 
//                                                                                                                                                                                                          
//        String xmlResponse = sendUsageRequest(xmlRequest);                                                                                                                                                
//        return checkResponse(xmlResponse, errorKeyAndValue, key, value);                                                                                                                                  
//    }                                                                                                                                                                                                     


    /*
     * XML utils
     */

//    private String replaceXmlTag(String xml, String oldTag, String newTag) {
//        return xml.replaceAll(oldTag, newTag);
//    }

    private String replaceXmlValue(String xml, String marker, String value) {
        marker = "\\s*%" + marker + "%\\s*";

        if (value == null) {
            value = "";
        }

        return xml.replaceAll(marker, value);
    }

//    private String extractXml(String xml, String marker) {
//        String startMarker = "<" + marker + ">";
//        String endMarker = "</" + marker + ">";
//        if (xml.contains(startMarker) && xml.contains(endMarker)) {
//            return xml.substring(xml.indexOf(startMarker) + startMarker.length(), xml.indexOf(endMarker));
//        } else {
//            return null;
//        }
//
//    }

//    private String setDelete(String xml, boolean delete) {
//        if (delete) {
//            String deleteMarker = " delete=\"delete\"";
//            xml = replaceXmlTag(xml, "get-configuration", "load-configuration");
//            xml = replaceXmlValue(xml, "delete", deleteMarker);
//        } else {
//            xml = replaceXmlTag(xml, "load-configuration", "get-configuration");
//            xml = replaceXmlValue(xml, "delete", "");
//        }
//
//        return xml;
//    }

    /*
     * Misc
     */    
    
//    private Long getVlanTag(String vlan) throws ExecutionException {
//        Long publicVlanTag = null;
//        if (!vlan.equals("untagged")) {
//            try {
//                publicVlanTag = Long.parseLong(vlan);
//            } catch (Exception e) {
//                throw new ExecutionException("Unable to parse VLAN tag: " + vlan);
//            }
//        }
//        
//        return publicVlanTag;
//    }
    
//    private String genObjectName(String... args) {
//        String objectName = "";
//
//        for (int i = 0; i < args.length; i++) {
//            objectName += args[i];
//            if (i != args.length -1) {
//                objectName += _objectNameWordSep;
//            }
//        }
//
//        return objectName;          
//    }


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
