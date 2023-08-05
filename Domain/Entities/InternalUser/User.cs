using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using AlfaCoreDumped.Domain.Entities.InternalUser.UserSolicitation;
using AlfaCoreDumped.Domain.ValueObject;

namespace AlfaCoreDumped.Domain.Entities.InternalUser
{
    public class User
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        public string UserName { get; set; }

        [Required]
        public string Password { get; set; }

        [Required]
        public string Cpf { get; set; }

        [Required]
        [RegularExpression("^[MFO]$", ErrorMessage = "Gender must be 'M', 'F', or 'O'.")]
        public char Gender { get; set; }

        [Required]
        public string RoleName { get; set; }

        [Required]
        public string RoleId { get; set; }

        [Required]
        public string Cbo { get; set; }

        public ICollection<Permission> Permissions { get; set; }
            = new List<Permission>();

        public ICollection<VacationSolicitationId> VacationSolicitationsIds { get; set; }
            = new List<VacationSolicitationId>();

        [ForeignKey("VacationSolicitationsIds")]
        public ICollection<VacationSolicitation> VacationSolicitations { get; set; }
            = new List<VacationSolicitation>();

        public ICollection<RescissionSolicitationId> RescissionSolicitationsIds { get; set; }
            = new List<RescissionSolicitationId>();

        [ForeignKey("RescissionSolicitationsIds")]
        public ICollection<RescissionSolicitation> RescissionSolicitations { get; set; }
            = new List<RescissionSolicitation>();
    }
}