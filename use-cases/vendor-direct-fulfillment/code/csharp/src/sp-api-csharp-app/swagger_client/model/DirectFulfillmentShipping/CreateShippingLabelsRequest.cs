/* 
 * Selling Partner API for Direct Fulfillment Shipping
 *
 * The Selling Partner API for Direct Fulfillment Shipping provides programmatic access to a direct fulfillment vendor's shipping data.
 *
 * OpenAPI spec version: 2021-12-28
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = spApiCsharpApp.swaggerClient.Client.SwaggerDateConverter;

namespace spApiCsharpApp.swaggerClient.Model.DirectFulfillmentShipping
{
    /// <summary>
    /// The request body for the createShippingLabels operation.
    /// </summary>
    [DataContract]
    public partial class CreateShippingLabelsRequest :  IEquatable<CreateShippingLabelsRequest>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CreateShippingLabelsRequest" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected CreateShippingLabelsRequest() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="CreateShippingLabelsRequest" /> class.
        /// </summary>
        /// <param name="sellingParty">ID of the selling party or vendor. (required).</param>
        /// <param name="shipFromParty">Warehouse code of vendor. (required).</param>
        /// <param name="containers">A list of the packages in this shipment..</param>
        public CreateShippingLabelsRequest(PartyIdentification sellingParty = default(PartyIdentification), PartyIdentification shipFromParty = default(PartyIdentification), List<Container> containers = default(List<Container>))
        {
            // to ensure "sellingParty" is required (not null)
            if (sellingParty == null)
            {
                throw new InvalidDataException("sellingParty is a required property for CreateShippingLabelsRequest and cannot be null");
            }
            else
            {
                this.SellingParty = sellingParty;
            }
            // to ensure "shipFromParty" is required (not null)
            if (shipFromParty == null)
            {
                throw new InvalidDataException("shipFromParty is a required property for CreateShippingLabelsRequest and cannot be null");
            }
            else
            {
                this.ShipFromParty = shipFromParty;
            }
            this.Containers = containers;
        }
        
        /// <summary>
        /// ID of the selling party or vendor.
        /// </summary>
        /// <value>ID of the selling party or vendor.</value>
        [DataMember(Name="sellingParty", EmitDefaultValue=false)]
        public PartyIdentification SellingParty { get; set; }

        /// <summary>
        /// Warehouse code of vendor.
        /// </summary>
        /// <value>Warehouse code of vendor.</value>
        [DataMember(Name="shipFromParty", EmitDefaultValue=false)]
        public PartyIdentification ShipFromParty { get; set; }

        /// <summary>
        /// A list of the packages in this shipment.
        /// </summary>
        /// <value>A list of the packages in this shipment.</value>
        [DataMember(Name="containers", EmitDefaultValue=false)]
        public List<Container> Containers { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class CreateShippingLabelsRequest {\n");
            sb.Append("  SellingParty: ").Append(SellingParty).Append("\n");
            sb.Append("  ShipFromParty: ").Append(ShipFromParty).Append("\n");
            sb.Append("  Containers: ").Append(Containers).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as CreateShippingLabelsRequest);
        }

        /// <summary>
        /// Returns true if CreateShippingLabelsRequest instances are equal
        /// </summary>
        /// <param name="input">Instance of CreateShippingLabelsRequest to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(CreateShippingLabelsRequest input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.SellingParty == input.SellingParty ||
                    (this.SellingParty != null &&
                    this.SellingParty.Equals(input.SellingParty))
                ) && 
                (
                    this.ShipFromParty == input.ShipFromParty ||
                    (this.ShipFromParty != null &&
                    this.ShipFromParty.Equals(input.ShipFromParty))
                ) && 
                (
                    this.Containers == input.Containers ||
                    this.Containers != null &&
                    this.Containers.SequenceEqual(input.Containers)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.SellingParty != null)
                    hashCode = hashCode * 59 + this.SellingParty.GetHashCode();
                if (this.ShipFromParty != null)
                    hashCode = hashCode * 59 + this.ShipFromParty.GetHashCode();
                if (this.Containers != null)
                    hashCode = hashCode * 59 + this.Containers.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}